const toggleButtons = document.querySelectorAll('button[id^="comment-toggle-"]');
const formContainers = document.querySelectorAll('div[id^="comment-form-"]');

toggleButtons.forEach(function(button) {
  const postId = button.id.split('-')[2];
  const formContainer = document.getElementById(`comment-form-${postId}`);

  button.addEventListener('click', function() {
    if (formContainer.style.display === 'none') {
      formContainer.style.display = 'block';
    } else {
      formContainer.style.display = 'none';
    }
  });
});