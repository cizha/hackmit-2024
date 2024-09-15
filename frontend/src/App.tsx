// app.tsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import Dropdown from 'react-bootstrap/Dropdown';


const App: React.FC = () => {
  const navigate = useNavigate();
  const [gameMode, setGameMode] = useState<string>('Prime-Number');

  const goToApp = () => {
    // Make a request to create the game first
    fetch('/scrabble/create-game')
      .then((res) => {
        if (res.ok) {
          // Navigate to '/scrabble' once the game is created
          navigate('/scrabble', { state: { mode: gameMode } });
        } else {
          // Handle error if the game creation fails
          alert("Failed to create game. Try again.");
        }
      });
  };

  const handleSelect = (eventKey: string | null) => {
    if (eventKey) {
      setGameMode(eventKey); // Update the game mode based on selected dropdown value
    }
  };

  return (
    <div className="main-container">
      <h1>Welcome to Scrabble Game</h1>

      {/* Dropdown for selecting game mode */}
      <div className="dropdown">
        <label htmlFor="game-mode">Select Game Mode: </label>
        <Dropdown onSelect={handleSelect}>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            {gameMode}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item eventKey="Prime-Number">Prime Number</Dropdown.Item>
            <Dropdown.Item eventKey="Multiples-Of-3">Multiples of 3</Dropdown.Item>
            <Dropdown.Item eventKey="Fibonacci-Sequence">Fibonacci Sequence</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </div>

      <div className="start">
      {/* Start game button */}
      <button onClick={goToApp} className="start-button">
        Start Game
      </button>
      </div>
    </div>
  );
};

export default App;
