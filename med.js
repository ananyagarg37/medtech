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

document.getElementById('signinForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const email = document.getElementById('signinEmail').value;
  const password = document.getElementById('signinPassword').value;
  const message = document.getElementById('signinMessage');  // Updated ID for message element

  // Simple validation for sign in (just an example)
  if (email && password) {
    message.style.color = "green";
    message.textContent = "Signin successful!";
    
    // Clear the form after successful submission
    document.getElementById('signinForm').reset();
  } else {
    message.style.color = "red";
    message.textContent = "Please fill in all fields!";
  }
});

