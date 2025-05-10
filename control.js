document.getElementById('waitingListForm').addEventListener('submit', async (e) => {
    e.preventDefault();
   // Get form inputs
    const name = document.getElementById('name').value.trim();
     const phone = document.getElementById('phone').value.trim();
    const email = document.getElementById('email').value.trim();
     // Client-side validation
    if (!name || name.length < 2) {
          alert('Please enter a valid name (at least 2 characters).');
      return;
    }
     const phoneRegex = /^\+?[\d\s-]{10,}$/;
    if (!phoneRegex.test(phone)) {
        alert('Please enter a valid phone number.');
      return;
    }
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
      return;
    }
       try {
      // Send data to backend
     const response = await fetch('http://localhost:5000/api/requests', {
        method: 'POST',
         headers: {
          'Content-Type': 'application/json',
              },
        body: JSON.stringify({ name, phone, email }),
          });
        const data = await response.json();
         if (response.ok) {
             alert('Request submitted successfully!');
        document.getElementById('waitingListForm').reset();
             } else {
        alert(data.message || 'Error submitting request.');
      }
  } catch (error) {
      console.error('Submission error:', error);
      alert('Server error. Please try again later.');
    }
  });
