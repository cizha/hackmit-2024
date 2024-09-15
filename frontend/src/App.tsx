// app.tsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';

const App: React.FC = () => {
  const navigate = useNavigate();
  const [gameMode, setGameMode] = useState<string>('PrimeNumber');

  const goToApp = () => {
    navigate('/scrabble', { state: { mode: gameMode } }); // Navigate to App component
  };

  return (
    <div className="main-container">
      <h1>Welcome to Scrabble Game</h1>

      {/* Dropdown for selecting game mode */}
      <div className="dropdown">
        <label htmlFor="game-mode">Select Game Mode: </label>
        <select
          id="game-mode"
          value={gameMode}
          onChange={(e) => setGameMode(e.target.value)}
        >
          <option value="PrimeNumber">Prime Number</option>
          <option value="MultiplesOf3">Multiples of 3</option>
          <option value="FibonacciSequence">Fibonacci Sequence</option>
        </select>
      </div>

      {/* Start game button */}
      <button onClick={goToApp} className="start-button">
        Start Game
      </button>
    </div>
  );
};

export default App;
