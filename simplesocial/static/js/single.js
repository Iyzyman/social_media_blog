const btn = document.getElementById('comment-toggle-{{ post.pk }}');
const tog = document.getElementById('comment-form-{{ post.pk }}');

btn.addEventListener('click', function() {
  if (tog.style.display === 'none') {
    tog.style.display = 'block';
  } else {
    tog.style.display = 'none';
  }
});