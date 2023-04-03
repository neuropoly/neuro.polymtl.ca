document.addEventListener("DOMContentLoaded", function () {
  const labels = document.querySelectorAll(".label");
  const publications = document.querySelectorAll(".publication");
  const filterBox = document.getElementById("filter-box");
  let activeLabels = new Set();

  function filterPublications() {
    publications.forEach((publication) => {
      const publicationLabels = publication.getAttribute("data-labels").split(" ");
      if (Array.from(activeLabels).every((label) => publicationLabels.includes(label))) {
        publication.style.display = "block";
      } else {
        publication.style.display = "none";
      }
    });
  }

  labels.forEach((label) => {
    label.addEventListener("click", function () {
      const selectedLabel = label.getAttribute("data-label");

      if (activeLabels.has(selectedLabel)) {
        activeLabels.delete(selectedLabel);
        label.classList.remove("active");
      } else {
        activeLabels.add(selectedLabel);
        label.classList.add("active");
      }

      filterBox.innerHTML = Array.from(activeLabels)
        .map((label) => `<span class="filter-label">${label}</span>`)
        .join(" ");

      filterPublications();
    });
  });
});
