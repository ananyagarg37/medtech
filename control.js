document.getElementById('waitingListForm').addEventListener('submit', async (e) => {
    e.preventDefault();
   // Get form inputs
    const name = document.getElementById('name').value.trim();
     const phone = document.getElementById('phone').value.trim();
    const email = document.getElementById('email').value.trim();
