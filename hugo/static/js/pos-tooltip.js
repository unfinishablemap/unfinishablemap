/*
 * Hover/focus cards for positions-register references.
 *
 * Anchors are marked up by layouts/_default/_markup/render-link.html, which
 * carries the claim and calibration bands as data attributes — so there is no
 * fetch, nothing to load, and the card works with the page offline.
 *
 * One card element is reused for every reference rather than one per link;
 * dense apex pages carry 28+ references.
 */
(function () {
  "use strict";

  var SHOW_DELAY = 120;
  var HIDE_DELAY = 180;
  var card = null;
  var showTimer = null;
  var hideTimer = null;
  var current = null;

  function build() {
    if (card) return card;
    card = document.createElement("div");
    card.className = "pos-card";
    card.setAttribute("role", "tooltip");
    card.hidden = true;
    // Keep the card open while the pointer is inside it, so links in a card
    // stay reachable and a slightly-off mouse path does not dismiss it.
    card.addEventListener("mouseenter", function () {
      window.clearTimeout(hideTimer);
    });
    card.addEventListener("mouseleave", scheduleHide);
    document.body.appendChild(card);
    return card;
  }

  function render(link) {
    var el = build();
    var bands = (link.getAttribute("data-pos-bands") || "")
      .split("·")
      .map(function (b) { return b.trim(); })
      .filter(Boolean);

    var head = document.createElement("div");
    head.className = "pos-card-head";
    var id = document.createElement("span");
    id.className = "pos-card-id";
    id.textContent = link.getAttribute("data-pos-id") || "";
    var dom = document.createElement("span");
    dom.className = "pos-card-domain";
    dom.textContent = link.getAttribute("data-pos-domain") || "";
    head.appendChild(id);
    head.appendChild(dom);

    var claim = document.createElement("p");
    claim.className = "pos-card-claim";
    claim.textContent = link.getAttribute("data-pos-claim") || "";

    el.textContent = "";
    el.appendChild(head);
    el.appendChild(claim);

    if (bands.length) {
      var row = document.createElement("div");
      row.className = "pos-card-bands";
      var weak = link.getAttribute("data-pos-weak") === "yes";
      bands.forEach(function (b) {
        var chip = document.createElement("span");
        chip.className = "pos-chip";
        // The build marks which positions carry a band a reader should not
        // miss; match the label so only that band is flagged, not the whole row.
        if (weak && (b === "no independent evidence" || b === "confidence: low")) {
          chip.className += " pos-chip-weak";
        }
        chip.textContent = b;
        row.appendChild(chip);
      });
      el.appendChild(row);
    }
    return el;
  }

  function place(link) {
    var el = card;
    el.hidden = false;
    var r = link.getBoundingClientRect();
    var cr = el.getBoundingClientRect();
    var margin = 8;

    var left = r.left + window.scrollX;
    var maxLeft = window.scrollX + document.documentElement.clientWidth - cr.width - margin;
    if (left > maxLeft) left = maxLeft;
    if (left < window.scrollX + margin) left = window.scrollX + margin;

    // Prefer above; flip below when there is not room.
    var top = r.top + window.scrollY - cr.height - 10;
    if (r.top - cr.height - 10 < 0) top = r.bottom + window.scrollY + 10;

    el.style.left = left + "px";
    el.style.top = top + "px";
  }

  function show(link) {
    if (current === link && card && !card.hidden) return;
    current = link;
    render(link);
    place(link);
    card.classList.add("is-visible");
  }

  function scheduleShow(link) {
    window.clearTimeout(hideTimer);
    window.clearTimeout(showTimer);
    showTimer = window.setTimeout(function () { show(link); }, SHOW_DELAY);
  }

  function hide() {
    if (!card) return;
    card.classList.remove("is-visible");
    card.hidden = true;
    current = null;
  }

  function scheduleHide() {
    window.clearTimeout(showTimer);
    window.clearTimeout(hideTimer);
    hideTimer = window.setTimeout(hide, HIDE_DELAY);
  }

  function bind(link) {
    // The build emits title= so that no-JS readers and server-side markdown
    // converters still get the claim. With JS available the card supersedes it,
    // so move it aside to avoid two tooltips stacking on hover.
    var native = link.getAttribute("title");
    if (native) {
      link.setAttribute("data-pos-title", native);
      link.removeAttribute("title");
    }
    link.addEventListener("mouseenter", function () { scheduleShow(link); });
    link.addEventListener("mouseleave", scheduleHide);
    // Keyboard users get the card on focus; Escape dismisses it.
    link.addEventListener("focus", function () { show(link); });
    link.addEventListener("blur", scheduleHide);
  }

  function init() {
    var links = document.querySelectorAll("a.pos-ref[data-pos-claim]");
    if (!links.length) return;
    Array.prototype.forEach.call(links, bind);

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") hide();
    });
    // On touch there is no hover: the first tap opens the card, and the link
    // itself still works on a second tap or via the "open" affordance.
    document.addEventListener("touchstart", function (e) {
      var link = e.target.closest && e.target.closest("a.pos-ref[data-pos-claim]");
      if (link) {
        if (current !== link) { e.preventDefault(); show(link); }
      } else if (card && !card.contains(e.target)) {
        hide();
      }
    }, { passive: false });
    window.addEventListener("scroll", hide, { passive: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
