import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import './game.css';

const Game: React.FC = () => {
  const location = useLocation();
  const gameMode = location.state?.mode || 'PrimeNumber';

  const gridSize = 15 * 15;
  const [selectedCell, setSelectedCell] = useState<number | null>(null);
  const [grid, setGrid] = useState<number[]>(Array(gridSize).fill(0));
  const [playerAScore, setPlayerAScore] = useState<number>(0);
  const [playerBScore, setPlayerBScore] = useState<number>(0);
  const [round, setRound] = useState<number>(1);
  const [playerATiles, setPlayerATiles] = useState<number[]>(Array(7).fill(0));
  const [playerATile, setPlayerATile] = useState<number | null>(null);
  const [playerBTiles, setPlayerBTiles] = useState<number[]>(Array(7).fill(0));
  const [playerBTile, setPlayerBTile] = useState<number | null>(null);

  // Fetch initial game data from the backend
  useEffect(() => {
    fetch(`/scrabble/game-state?mode=${gameMode}`)
      .then((res) => res.json())
      .then((data) => {
        setGrid(data.grid);
        setPlayerAScore(data.playerAScore);
        setPlayerBScore(data.playerBScore);
        setRound(data.round);
        setPlayerATiles(data.playerATiles); 
        setPlayerBTiles(data.playerBTiles); 
      });
  }, []);

  const handleCellClick = (index: number) => {
    setSelectedCell(index); // Select a cell on the grid
  };

  const handleATileClick = (tile: number) => {
    setPlayerATile(tile); // Select a tile from Player A's tiles
  };

  const handleBTileClick = (tile: number) => {
    setPlayerBTile(tile); // Select a tile from Player B's tiles
  };

  const handleSubmit = () => {
    if (selectedCell !== null && playerATile !== null) {
      // Send the selected tile and cell to the backend for Player A
      fetch('/scrabble/update-game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          selectedCell,
          tile: playerATile,
          player: 'A',
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          // Update the game state after receiving response from backend
          setGrid(data.grid);
          setPlayerAScore(data.playerAScore);
          setPlayerBScore(data.playerBScore);
          setPlayerATiles(data.playerATiles); // New tiles for Player A
          setPlayerBTiles(data.playerBTiles); // New tiles for Player B
        });

      // Reset selections
      setPlayerATile(null);
      setSelectedCell(null);
    } else if (selectedCell !== null && playerBTile !== null) {
      // Send the selected tile and cell to the backend for Player B
      fetch('/scrabble/update-game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          selectedCell,
          tile: playerBTile,
          player: 'B',
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          // Update the game state after receiving response from backend
          setGrid(data.grid);
          setPlayerAScore(data.playerAScore);
          setPlayerBScore(data.playerBScore);
          setPlayerATiles(data.playerATiles); // New tiles for Player A
          setPlayerBTiles(data.playerBTiles); // New tiles for Player B
        });

      // Reset selections
      setPlayerBTile(null);
      setSelectedCell(null);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <h2>SCRABBLE - {gameMode.toUpperCase()} MODE</h2>
        <p>ROUND {round}</p>
      </div>

      <div className="game-container">
        {/* Player A's Scoreboard */}
        <div className="player-panel">
          <h3>Player A: {playerAScore} pts</h3>
          <div className="player-tiles">
            {playerATiles.map((tile, idx) => (
              <div
                key={idx}
                className={`tile ${playerATile === idx ? 'selected' : ''}`}
                onClick={() => handleATileClick(idx)} // Select a tile when clicked
              >
                {tile}
              </div>
            ))}
          </div>
        </div>

        {/* Game Board */}
        <div className="grid-board">
          {grid.map((cellValue, index) => (
            <div
              key={index}
              className={`grid-item ${selectedCell === index ? 'selected' : ''}`}
              onClick={() => handleCellClick(index)} // Select a cell on the grid
            >
              {cellValue !== 0 ? cellValue : "*"}
            </div>
          ))}
        </div>

        {/* Player B's Scoreboard */}
        <div className="player-panel">
          <h3>Player B: {playerBScore} pts</h3>
          <div className="player-tiles">
            {playerBTiles.map((tile, idx) => (
              <div
                key={idx}
                className={`tile ${playerBTile === idx ? 'selected' : ''}`}
                onClick={() => handleBTileClick(idx)} // Select a tile for Player B
              >
                {tile}
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Submit Button at the Bottom */}
      <div className = "bottom">
        <div className="submit-button">
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>
    </div>
  );
};

export default Game;
