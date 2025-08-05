
const form = document.getElementById('product-form');
const resultDiv = document.getElementById('result');
const copyPre = document.getElementById('copy');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const product = {
        name: formData.get('name'),
        description: formData.get('description'),
        target_audience: formData.get('target_audience'),
    };

    const response = await fetch('/generate-copy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(product),
    });

    const data = await response.json();

    copyPre.textContent = data.copy;
    resultDiv.style.display = 'block';
});
