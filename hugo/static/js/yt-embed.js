// Hydrate <details class="yt-embed" data-video-id="..."> placeholders into
// responsive lazy YouTube iframes. The placeholder anchor remains in the
// server-rendered HTML so the link is visible to non-JS clients and to
// Cloudflare's HTML→markdown serializer for AI agents. The summary/caption
// elements are preserved.
(function () {
    function hydrate(el) {
        if (el.dataset.ytHydrated === '1') return;
        var id = el.getAttribute('data-video-id');
        if (!id) return;
        var anchor = el.querySelector('a[href*="youtu"]');
        if (!anchor) return;

        var frame = document.createElement('div');
        frame.className = 'yt-frame';

        // Mirror YouTube's canonical embed markup exactly so the player
        // serves the standard chrome (controls, fullscreen, etc.).
        var iframe = document.createElement('iframe');
        iframe.setAttribute('src', 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id));
        iframe.setAttribute('title', 'YouTube video player');
        iframe.setAttribute('loading', 'lazy');
        iframe.setAttribute('frameborder', '0');
        iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
        iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
        iframe.setAttribute('allowfullscreen', '');

        frame.appendChild(iframe);
        anchor.replaceWith(frame);
        el.dataset.ytHydrated = '1';
        el.classList.add('yt-embed--hydrated');
    }

    function init() {
        document.querySelectorAll('.yt-embed[data-video-id]').forEach(hydrate);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
