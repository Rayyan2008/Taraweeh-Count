import React, { useState } from 'react';
import './App.css';
import { FaRedo, FaHome, FaPlus } from 'react-icons/fa'; // Importing icons from FontAwesome

function App() {
  const [rakatCount, setRakatCount] = useState(0);
  const [breakMessage, setBreakMessage] = useState('');
  const totalRakats = 20;

  const incrementRakat = () => {
    if (rakatCount + 2 <= totalRakats) {
      const newCount = rakatCount + 2;
      setRakatCount(newCount);

      // Show break reminder after every 4 rakats
      if (newCount % 4 === 0) {
        setBreakMessage('Take a short break!');
      } else {
        setBreakMessage('');
      }
    }
  };

  const resetRakat = () => {
    setRakatCount(0);
    setBreakMessage('');
  };

  return (
    <div className="App">
      <h1>Taraweeh Rakat Counter</h1>
      <div className="counter">
        <p>{`Rakat: ${rakatCount} / ${totalRakats}`}</p>
        {breakMessage && <p className="break-message">{breakMessage}</p>} {/* Display break message */}
        <div className="buttons">
          <button className="increment" onClick={incrementRakat}>
            <FaPlus /> Next Rakat
          </button>
          <button className="reset" onClick={resetRakat}>
            <FaRedo /> Reset
          </button>
          <button className="home">
            <FaHome /> Home
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
