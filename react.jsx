import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [engineTemp, setEngineTemp] = useState('');
  const [rpm, setRpm] = useState('');
  const [speed, setSpeed] = useState('');
  const [errorCode, setErrorCode] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('/diagnose', {
      engine_temp: engineTemp,
      rpm: rpm,
      speed: speed,
      error_code: errorCode,
    });
    setResult(response.data.fault);
  };

  return (
    <div>
      <h1>Vehicle Fault Diagnosis</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Engine Temp" value={engineTemp} onChange={(e) => setEngineTemp(e.target.value)} />
        <input type="text" placeholder="RPM" value={rpm} onChange={(e) => setRpm(e.target.value)} />
        <input type="text" placeholder="Speed" value={speed} onChange={(e) => setSpeed(e.target.value)} />
        <input type="text" placeholder="Error Code" value={errorCode} onChange={(e) => setErrorCode(e.target.value)} />
        <button type="submit">Diagnose</button>
      </form>
      {result && <div>Diagnosis Result: {result}</div>}
    </div>
  );
}

export default App;
