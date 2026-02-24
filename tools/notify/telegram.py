"""Telegram logging handler with digest-based rate limiting.

Forwards ERROR+ log messages to a Telegram chat, batching them into
digests so that at most one Telegram message is sent per hour.

Pacing algorithm (three-phase state machine):

    IDLE  -- first error -->  GRACE (30s timer)
    GRACE -- timer fires  -->  send digest, COOLDOWN (1h timer)
    COOLDOWN -- timer fires, buffer non-empty -->  send digest, restart COOLDOWN
    COOLDOWN -- timer fires, buffer empty     -->  IDLE
"""

import atexit
import logging
import os
import platform
import sys
import threading
import time
from collections import deque
from datetime import datetime, timezone
from enum import Enum, auto
from pathlib import Path
from typing import NamedTuple

import httpx
from dotenv import load_dotenv

# Load .env from project root
_env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(_env_path)

# Environment variable names
TELEGRAM_BOT_TOKEN_ENV = "TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID_ENV = "TELEGRAM_CHAT_ID"

TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"
TELEGRAM_MAX_MESSAGE_LENGTH = 4096


class BufferedError(NamedTuple):
    """A buffered log record summary."""

    timestamp: float  # time.monotonic()
    level_name: str
    message: str
    logger_name: str


class _Phase(Enum):
    """State machine phases for the pacing algorithm."""

    IDLE = auto()
    GRACE = auto()
    COOLDOWN = auto()


class TelegramHandler(logging.Handler):
    """Logging handler that sends ERROR+ messages to Telegram as digests.

    Args:
        bot_token: Telegram bot token. Falls back to TELEGRAM_BOT_TOKEN env var.
        chat_id: Telegram chat ID. Falls back to TELEGRAM_CHAT_ID env var.
        grace_seconds: How long to wait after the first error before sending.
        cooldown_seconds: Minimum interval between Telegram messages.
        max_buffer_size: Maximum buffered errors (oldest dropped when full).
    """

    def __init__(
        self,
        bot_token: str | None = None,
        chat_id: str | None = None,
        grace_seconds: float = 30.0,
        cooldown_seconds: float = 3600.0,
        max_buffer_size: int = 100,
    ) -> None:
        super().__init__(level=logging.ERROR)

        self._bot_token = bot_token or os.environ.get(TELEGRAM_BOT_TOKEN_ENV)
        self._chat_id = chat_id or os.environ.get(TELEGRAM_CHAT_ID_ENV)
        self._enabled = bool(self._bot_token and self._chat_id)

        self._grace_seconds = grace_seconds
        self._cooldown_seconds = cooldown_seconds
        self._max_buffer_size = max_buffer_size

        self._lock = threading.Lock()
        self._buffer: deque[BufferedError] = deque()
        self._dropped_count: int = 0
        self._phase: _Phase = _Phase.IDLE
        self._timer: threading.Timer | None = None
        self._closed = False

        if self._enabled:
            atexit.register(self.close)

    def is_enabled(self) -> bool:
        """Whether the handler has credentials and will actually send."""
        return self._enabled

    def emit(self, record: logging.LogRecord) -> None:
        """Buffer an error record. Never does I/O."""
        if not self._enabled:
            return

        try:
            entry = BufferedError(
                timestamp=time.monotonic(),
                level_name=record.levelname,
                message=self.format(record),
                logger_name=record.name,
            )

            with self._lock:
                if self._closed:
                    return

                if len(self._buffer) >= self._max_buffer_size:
                    self._buffer.popleft()
                    self._dropped_count += 1
                self._buffer.append(entry)

                if self._phase == _Phase.IDLE:
                    self._phase = _Phase.GRACE
                    self._schedule_timer(self._grace_seconds)
        except Exception:
            self.handleError(record)

    def flush(self) -> None:
        """Flush buffered errors immediately, bypassing grace/cooldown."""
        with self._lock:
            if self._timer is not None:
                self._timer.cancel()
                self._timer = None

            errors = list(self._buffer)
            dropped = self._dropped_count
            self._buffer.clear()
            self._dropped_count = 0
            self._phase = _Phase.IDLE

        if errors:
            text = self._format_digest(errors, dropped)
            self._send_telegram(text)

    def close(self) -> None:
        """Flush remaining errors and clean up."""
        with self._lock:
            if self._closed:
                return
            self._closed = True

        self.flush()

        try:
            atexit.unregister(self.close)
        except Exception:
            pass

        super().close()

    def _schedule_timer(self, delay: float) -> None:
        """Schedule _on_timer after delay seconds. Must hold self._lock."""
        if self._timer is not None:
            self._timer.cancel()
        self._timer = threading.Timer(delay, self._on_timer)
        self._timer.daemon = True
        self._timer.start()

    def _on_timer(self) -> None:
        """Timer callback: decide whether to send and what phase to enter next."""
        with self._lock:
            if self._closed:
                return

            errors = list(self._buffer)
            dropped = self._dropped_count
            self._buffer.clear()
            self._dropped_count = 0

            if self._phase == _Phase.GRACE:
                self._phase = _Phase.COOLDOWN
                self._schedule_timer(self._cooldown_seconds)
            elif self._phase == _Phase.COOLDOWN:
                if errors:
                    self._schedule_timer(self._cooldown_seconds)
                else:
                    self._phase = _Phase.IDLE
                    self._timer = None

        # Send outside the lock so emit() isn't blocked during HTTP
        if errors:
            text = self._format_digest(errors, dropped)
            self._send_telegram(text)

    def _format_digest(self, errors: list[BufferedError], dropped: int) -> str:
        """Format buffered errors into a Telegram message."""
        now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        hostname = platform.node()
        count = len(errors)

        header = (
            f"\U0001f534 Unfinishable Map \u2014 {count} error{'s' if count != 1 else ''}\n"
            f"{now_utc} | {hostname}\n"
        )

        body_parts: list[str] = []
        for err in errors:
            msg = err.message[:300]
            if len(err.message) > 300:
                msg += "..."
            body_parts.append(f"\u2022 [{err.level_name}] {msg}")

        body = "\n".join(body_parts)

        footer = ""
        if dropped > 0:
            plural = "s" if dropped != 1 else ""
            footer = f"\n\u26a0\ufe0f {dropped} additional error{plural} dropped (buffer full)"

        full = header + "\n" + body + footer

        if len(full) > TELEGRAM_MAX_MESSAGE_LENGTH:
            truncation_note = "\n... (truncated)"
            max_body = (
                TELEGRAM_MAX_MESSAGE_LENGTH - len(header) - len(footer) - len(truncation_note) - 1
            )
            body = body[:max_body] + truncation_note
            full = header + "\n" + body + footer

        return full

    def _send_telegram(self, text: str) -> bool:
        """Send a message via Telegram Bot API. Returns True on success."""
        url = TELEGRAM_API_URL.format(token=self._bot_token)
        payload = {
            "chat_id": self._chat_id,
            "text": text,
        }

        try:
            response = httpx.post(url, json=payload, timeout=10.0)
            if response.status_code == 200:
                return True
            self._fallback_log(
                f"Telegram API returned {response.status_code}: {response.text[:200]}"
            )
            return False
        except httpx.RequestError as e:
            self._fallback_log(f"Telegram API request failed: {e}")
            return False
        except Exception as e:
            self._fallback_log(f"Telegram send unexpected error: {e}")
            return False

    @staticmethod
    def _fallback_log(message: str) -> None:
        """Write to stderr directly, avoiding recursive logging."""
        try:
            print(f"[TelegramHandler] {message}", file=sys.stderr, flush=True)
        except Exception:
            pass
