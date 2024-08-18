document.getElementById('diagnosis-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const engineTemp = document.getElementById('engineTemp').value;
    const rpm = document.getElementById('rpm').value;
    const speed = document.getElementById('speed').value;
    const errorCode = document.getElementById('errorCode').value;

    const data = {
        engine_temp: engineTemp,
        rpm: rpm,
        speed: speed,
        error_code: errorCode
    };

    fetch('http://127.0.0.1:5000/diagnose', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Diagnosis Result: ' + data.fault;
    })
    .catch(error => console.error('Error:', error));
});
