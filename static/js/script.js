document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('essayForm');
  const output = document.getElementById('output');
  const resultBox = document.getElementById('aiOutput');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form values
    const type = document.getElementById('typeSelect').value.trim();
    const topic = document.getElementById('topic').value.trim();
    const draft = document.getElementById('draft').value.trim();

    try {
      // Send data to server
      const response = await fetch('/polish_essay', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type, topic, draft })
      });

      const data = await response.json();

      // Show result or error
      resultBox.innerText = data.result || data.error || "Unexpected error occurred.";
      output.classList.remove('d-none');

    } catch (error) {
      resultBox.innerText = "Network error or server issue.";
      output.classList.remove('d-none');
    }
  });
});
