// Open Journalist website: mobile navigation and tabs. No tracking, no third-party code.
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Tabs: <div class="tabs"><div class="tab-list" role="tablist"><button role="tab" aria-controls="id">…
  document.querySelectorAll(".tabs").forEach(function (tabs) {
    var buttons = tabs.querySelectorAll('[role="tab"]');
    function select(btn) {
      buttons.forEach(function (b) {
        var on = b === btn;
        b.setAttribute("aria-selected", on ? "true" : "false");
        b.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(b.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
    }
    buttons.forEach(function (btn, i) {
      btn.addEventListener("click", function () { select(btn); });
      btn.addEventListener("keydown", function (e) {
        if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
        var next = buttons[(i + (e.key === "ArrowRight" ? 1 : buttons.length - 1)) % buttons.length];
        select(next); next.focus();
      });
    });
    // Preselect the visitor's platform for install instructions.
    var mac = /Mac/i.test(navigator.platform || navigator.userAgent);
    var pref = tabs.querySelector('[data-platform="' + (mac ? "mac" : "win") + '"]');
    if (pref) select(pref);
  });
})();
