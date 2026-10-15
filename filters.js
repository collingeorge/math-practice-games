// Skill filter buttons on the Math and Reading pages.
// Hides game cards whose data-skill does not match, and hides any level left empty.
(function () {
  "use strict";
  var group = document.querySelector(".filters");
  if (!group) return;
  var buttons = group.querySelectorAll("button[data-filter]");
  var cards = document.querySelectorAll(".games > li[data-skill]");
  var levels = document.querySelectorAll(".level");

  function apply(filter) {
    buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.filter === filter)); });
    cards.forEach(function (c) { c.classList.toggle("hidden", filter !== "all" && c.dataset.skill !== filter); });
    levels.forEach(function (lv) { lv.classList.toggle("hidden", !lv.querySelector(".games > li:not(.hidden)")); });
  }

  group.addEventListener("click", function (e) {
    var b = e.target.closest("button[data-filter]");
    if (b) apply(b.dataset.filter);
  });
})();
