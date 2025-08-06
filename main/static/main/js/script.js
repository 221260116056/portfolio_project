// Fade-in cards on scroll
document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll('.card');

  // Create observer instance
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        entry.target.classList.remove('invisible'); // Remove invisible class once faded in
      }
    });
  }, {
    threshold: 0.1 // Trigger when 10% of the element is visible
  });

  // Apply to each card
  cards.forEach(card => {
    card.classList.add('invisible');  // Start hidden
    observer.observe(card);           // Observe for scroll into view
  });
});
