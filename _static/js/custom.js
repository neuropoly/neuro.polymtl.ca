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
});
