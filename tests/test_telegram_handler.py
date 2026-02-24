"""Tests for the Telegram logging handler with digest-based rate limiting."""

import logging
import time
from unittest.mock import MagicMock, patch

from tools.notify.telegram import BufferedError, TelegramHandler, _Phase

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_record(
    msg: str = "something failed",
    level: int = logging.ERROR,
    name: str = "test",
) -> logging.LogRecord:
    """Create a minimal LogRecord."""
    return logging.LogRecord(
        name=name,
        level=level,
        pathname="test.py",
        lineno=1,
        msg=msg,
        args=(),
        exc_info=None,
    )


def _make_handler(**kwargs: object) -> TelegramHandler:
    """Create a handler with fake credentials and no real timers."""
    defaults = {
        "bot_token": "fake-token",
        "chat_id": "12345",
        "grace_seconds": 30.0,
        "cooldown_seconds": 3600.0,
    }
    defaults.update(kwargs)
    return TelegramHandler(**defaults)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Configuration / enable tests
# ---------------------------------------------------------------------------

class TestConfiguration:
    def test_disabled_without_credentials(self) -> None:
        handler = TelegramHandler(bot_token=None, chat_id=None)
        assert not handler.is_enabled()

    def test_disabled_with_partial_credentials(self) -> None:
        handler = TelegramHandler(bot_token="tok", chat_id=None)
        assert not handler.is_enabled()

    def test_enabled_with_both_credentials(self) -> None:
        handler = _make_handler()
        assert handler.is_enabled()
        handler.close()

    def test_emit_noop_when_disabled(self) -> None:
        handler = TelegramHandler(bot_token=None, chat_id=None)
        record = _make_record()
        handler.emit(record)
        assert len(handler._buffer) == 0


# ---------------------------------------------------------------------------
# Emit / buffering tests
# ---------------------------------------------------------------------------

class TestEmit:
    def test_buffers_error(self) -> None:
        handler = _make_handler()
        handler.emit(_make_record("error one"))
        assert len(handler._buffer) == 1
        assert handler._buffer[0].message == "error one"
        handler.close()

    def test_transitions_to_grace_on_first_error(self) -> None:
        handler = _make_handler()
        handler.emit(_make_record())
        assert handler._phase == _Phase.GRACE
        assert handler._timer is not None
        handler.close()

    def test_stays_in_grace_on_subsequent_errors(self) -> None:
        handler = _make_handler()
        handler.emit(_make_record("one"))
        handler.emit(_make_record("two"))
        handler.emit(_make_record("three"))
        assert handler._phase == _Phase.GRACE
        assert len(handler._buffer) == 3
        handler.close()

    def test_buffer_overflow_drops_oldest(self) -> None:
        handler = _make_handler(max_buffer_size=3)
        for i in range(5):
            handler.emit(_make_record(f"error {i}"))
        assert len(handler._buffer) == 3
        assert handler._dropped_count == 2
        messages = [e.message for e in handler._buffer]
        assert messages == ["error 2", "error 3", "error 4"]
        handler.close()

    def test_emit_does_not_buffer_after_close(self) -> None:
        handler = _make_handler()
        handler.close()
        handler.emit(_make_record())
        assert len(handler._buffer) == 0


# ---------------------------------------------------------------------------
# State machine / timer tests
# ---------------------------------------------------------------------------

class TestStateMachine:
    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_grace_timer_sends_and_enters_cooldown(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("first error"))

        # Cancel the real timer and fire _on_timer manually
        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()

        mock_send.assert_called_once()
        assert handler._phase == _Phase.COOLDOWN
        handler.close()

    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_cooldown_buffers_without_sending(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("first"))

        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()
        mock_send.reset_mock()

        # Now in COOLDOWN — new errors should buffer but not send
        handler.emit(_make_record("second"))
        assert len(handler._buffer) == 1
        mock_send.assert_not_called()
        handler.close()

    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_cooldown_timer_sends_if_buffer_nonempty(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("first"))

        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()
        mock_send.reset_mock()

        # Buffer more errors during cooldown
        handler.emit(_make_record("second"))

        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()

        mock_send.assert_called_once()
        assert handler._phase == _Phase.COOLDOWN
        handler.close()

    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_cooldown_timer_returns_to_idle_if_empty(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("first"))

        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()
        mock_send.reset_mock()

        # No new errors during cooldown
        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()

        mock_send.assert_not_called()
        assert handler._phase == _Phase.IDLE
        handler.close()

    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_idle_after_cooldown_accepts_new_errors(self, mock_send: MagicMock) -> None:
        handler = _make_handler()

        # IDLE -> GRACE -> COOLDOWN -> IDLE
        handler.emit(_make_record("first"))
        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()
        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()
        assert handler._phase == _Phase.IDLE

        # New error should restart the cycle
        handler.emit(_make_record("new cycle"))
        assert handler._phase == _Phase.GRACE
        assert len(handler._buffer) == 1
        handler.close()


# ---------------------------------------------------------------------------
# Digest formatting tests
# ---------------------------------------------------------------------------

class TestFormatDigest:
    def test_single_error(self) -> None:
        handler = _make_handler()
        errors = [BufferedError(time.monotonic(), "ERROR", "disk full", "evolve_loop")]
        text = handler._format_digest(errors, dropped=0)
        assert "1 error" in text
        assert "disk full" in text
        assert "dropped" not in text.lower()
        handler.close()

    def test_multiple_errors(self) -> None:
        handler = _make_handler()
        errors = [
            BufferedError(time.monotonic(), "ERROR", "err one", "a"),
            BufferedError(time.monotonic(), "CRITICAL", "err two", "b"),
        ]
        text = handler._format_digest(errors, dropped=0)
        assert "2 errors" in text
        assert "[ERROR]" in text
        assert "[CRITICAL]" in text
        handler.close()

    def test_dropped_count_shown(self) -> None:
        handler = _make_handler()
        errors = [BufferedError(time.monotonic(), "ERROR", "msg", "x")]
        text = handler._format_digest(errors, dropped=5)
        assert "5 additional errors dropped" in text
        handler.close()

    def test_long_message_truncated_per_entry(self) -> None:
        handler = _make_handler()
        long_msg = "x" * 500
        errors = [BufferedError(time.monotonic(), "ERROR", long_msg, "x")]
        text = handler._format_digest(errors, dropped=0)
        assert "..." in text
        # Individual entry should be capped at ~303 chars
        for line in text.split("\n"):
            if line.startswith("\u2022"):
                assert len(line) < 350
        handler.close()

    def test_total_message_within_telegram_limit(self) -> None:
        handler = _make_handler()
        errors = [
            BufferedError(time.monotonic(), "ERROR", "e" * 300, f"logger_{i}")
            for i in range(50)
        ]
        text = handler._format_digest(errors, dropped=0)
        assert len(text) <= 4096
        handler.close()


# ---------------------------------------------------------------------------
# Flush / close tests
# ---------------------------------------------------------------------------

class TestFlushClose:
    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_flush_sends_buffered_errors(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("one"))
        handler.emit(_make_record("two"))

        handler._timer.cancel()  # type: ignore[union-attr]
        handler.flush()

        mock_send.assert_called_once()
        assert len(handler._buffer) == 0
        assert handler._phase == _Phase.IDLE
        handler.close()

    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_close_flushes(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("buffered"))
        handler._timer.cancel()  # type: ignore[union-attr]
        handler.close()
        mock_send.assert_called_once()

    @patch.object(TelegramHandler, "_send_telegram", return_value=True)
    def test_double_close_is_safe(self, mock_send: MagicMock) -> None:
        handler = _make_handler()
        handler.emit(_make_record("x"))
        handler._timer.cancel()  # type: ignore[union-attr]
        handler.close()
        handler.close()  # Should not raise or send twice
        mock_send.assert_called_once()


# ---------------------------------------------------------------------------
# Telegram API tests (mocked HTTP)
# ---------------------------------------------------------------------------

class TestSendTelegram:
    @patch("tools.notify.telegram.httpx.post")
    def test_success(self, mock_post: MagicMock) -> None:
        mock_post.return_value = MagicMock(status_code=200)
        handler = _make_handler()
        assert handler._send_telegram("test message") is True
        mock_post.assert_called_once()
        handler.close()

    @patch("tools.notify.telegram.httpx.post")
    def test_api_error(self, mock_post: MagicMock) -> None:
        mock_post.return_value = MagicMock(status_code=500, text="Internal Server Error")
        handler = _make_handler()
        assert handler._send_telegram("test message") is False
        handler.close()

    @patch("tools.notify.telegram.httpx.post")
    def test_network_error(self, mock_post: MagicMock) -> None:
        import httpx

        mock_post.side_effect = httpx.ConnectError("connection refused")
        handler = _make_handler()
        assert handler._send_telegram("test message") is False
        handler.close()

    @patch("tools.notify.telegram.httpx.post")
    def test_no_recursive_logging(self, mock_post: MagicMock) -> None:
        """Verify that send failures don't trigger recursive logging."""
        mock_post.return_value = MagicMock(status_code=500, text="fail")

        handler = _make_handler()
        test_logger = logging.getLogger("test_recursion")
        test_logger.addHandler(handler)
        test_logger.setLevel(logging.ERROR)

        # This should not cause infinite recursion
        test_logger.error("trigger error")

        # Manually fire the timer to cause the send
        handler._timer.cancel()  # type: ignore[union-attr]
        handler._on_timer()

        # The send was attempted (and failed), but no recursion
        mock_post.assert_called_once()
        test_logger.removeHandler(handler)
        handler.close()
