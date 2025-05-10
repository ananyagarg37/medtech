document.getElementById('waitingListForm').addEventListener('submit', async (e) => {
    e.preventDefault();
   // Get form inputs
    const name = document.getElementById('name').value.trim();
