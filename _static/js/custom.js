<<<<<<< HEAD
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
=======
document.addEventListener('DOMContentLoaded', function () {
  const labels = document.getElementsByClassName('label');
  const publications = document.getElementsByClassName('publication');
  const filterBox = document.getElementById('filter-box');
  const selectedLabels = new Set();

  for (let label of labels) {
    label.addEventListener('click', () => addLabel(label));
  }

  function addLabel(labelElement) {
    const label = labelElement.getAttribute('data-label');
    if (!selectedLabels.has(label)) {
      selectedLabels.add(label);
      labelElement.classList.add('label-hidden');
      let newLabelElement = document.createElement('span');
      newLabelElement.textContent = label;
      newLabelElement.classList.add('selected-label', 'label');
      newLabelElement.addEventListener('click', () => removeLabel(label, newLabelElement, labelElement));
      filterBox.appendChild(newLabelElement);
      filterPublications();
    }
  }

  function removeLabel(label, newLabelElement, labelElement) {
    selectedLabels.delete(label);
    filterBox.removeChild(newLabelElement);
    labelElement.classList.remove('label-hidden');
    filterPublications();
  }

  function filterPublications() {
    for (let publication of publications) {
      const publicationLabels = publication.dataset.labels.split(' ').map(label => label.trim());
      let hasAnyLabel = selectedLabels.size === 0;

      for (const selectedLabel of selectedLabels) {
        if (publicationLabels.includes(selectedLabel)) {
          hasAnyLabel = true;
          break;
        }
      }

      if (hasAnyLabel) {
        publication.style.display = 'block';
      } else {
        publication.style.display = 'none';
      }
    }
  }
>>>>>>> a7eee3b44ec2c56273274d5674a7b75a84a6819e
});
