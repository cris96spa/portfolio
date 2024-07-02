document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector('.php-email-form');
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    
    let isValid = true;
    document.querySelectorAll('.form-control').forEach(input => {
      if (!input.value) {
        isValid = false;
        input.style.borderColor = 'red'; // Highlight fields that are empty
      } else {
        input.style.borderColor = '#ccc'; // Reset to default style if corrected
      }
    });

    if (isValid) {
      this.submit();
    }
  });
});