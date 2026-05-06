document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        age: document.getElementById('age').value,
        sex: document.getElementById('sex').value,
        bmi: document.getElementById('bmi').value,
        children: document.getElementById('children').value,
        smoker: document.getElementById('smoker').value,
        region: document.getElementById('region').value
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (response.ok) {
            displayResult(data.prediction);
            hideError();
        } else {
            showError(data.error || 'An error occurred');
        }
    } catch (error) {
        showError('Failed to connect to the server. Please try again.');
    }
});

function displayResult(premium) {
    document.getElementById('premiumValue').textContent = premium.toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
    document.getElementById('result').classList.remove('hidden');
    document.querySelector('.form-container').style.display = 'none';
}

function resetForm() {
    document.getElementById('predictionForm').reset();
    document.getElementById('result').classList.add('hidden');
    document.querySelector('.form-container').style.display = 'flex';
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

function hideError() {
    document.getElementById('error').classList.add('hidden');
}
