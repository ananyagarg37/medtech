document.getElementById('signupForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;
  const message = document.getElementById('message');

  if (password !== confirmPassword) {
    message.style.color = "red";
    message.textContent = "Passwords do not match!";
  } else {
    message.style.color = "green";
    message.textContent = "Signup successful!";
    
    // ✅ Clear the form after successful submission
    document.getElementById('signupForm').reset();
  }
});
