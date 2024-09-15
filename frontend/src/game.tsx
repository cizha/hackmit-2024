import React, { useState, useEffect, useRef } from 'react';
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

  const [playerATiles, setPlayerATiles] = useState<{ index: number; value: number }[]>(Array(7).fill({ index: 0, value: 0 }));
  const [playerATile, setPlayerATile] = useState<{ index: number; value: number } | null>(null);
  const [playerBTiles, setPlayerBTiles] = useState<{ index: number; value: number }[]>(Array(7).fill({ index: 0, value: 0 }));
  const [playerBTile, setPlayerBTile] = useState<{ index: number; value: number } | null>(null);

  // Fetch initial game data from the backend

  const constantRef = useRef(location.state?.mode || 'PrimeNumber'); // Initialize with a constant value

  const local = "http://localhost:3000"

  useEffect(() => {
    fetch(local+`/scrabble/game-state?mode=${constantRef.current}) //gameMode}`)
      .then((res) => res.json())
      .then((data) => {
        setGrid(data.grid);
        setPlayerAScore(data.playerAScore);
        setPlayerBScore(data.playerBScore);
        setRound(data.round);
        setPlayerATiles(data.playerATiles.map((value: number, index: number) => ({ index, value })));
        setPlayerBTiles(data.playerBTiles.map((value: number, index: number) => ({ index, value })));
      });
  }, []); 

  const handleCellClick = (index: number) => {
    setSelectedCell(index); // Select a cell on the grid
  };

  const handleATileClick = (tile: { index: number; value: number }) => {
    setPlayerATile(tile); // Select a tile from Player A's tiles
  };

  const handleBTileClick = (tile: { index: number; value: number }) => {
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
          mode: gameMode,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          // Update the game state after receiving response from backend
          setGrid(data.grid);
          setPlayerAScore(data.playerAScore);
          setPlayerBScore(data.playerBScore);
          setPlayerATiles(data.playerA.tiles.map((value: number, index: number) => ({ index, value })));
          setPlayerBTiles(data.playerB.tiles.map((value: number, index: number) => ({ index, value })));
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
          mode: gameMode,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          // Update the game state after receiving response from backend
          setGrid(data.grid);
          setPlayerAScore(data.playerAScore);
          setPlayerBScore(data.playerBScore);
          setPlayerATiles(data.playerA.tiles.map((value: number, index: number) => ({ index, value })));
          setPlayerBTiles(data.playerB.tiles.map((value: number, index: number) => ({ index, value })));
        });

      // Reset selections
      setPlayerBTile(null);
      setSelectedCell(null);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <h2>SCRABBLE : {gameMode.toUpperCase()} MODE</h2>
        <p>ROUND {round}</p>
      </div>

      <div className="game-container">
        {/* Player A's Scoreboard */}
        <div className="player-panel">
          <h3>Player A: {playerAScore} pts</h3>
          <div className="player-tiles">
              {playerBTiles.map((tile) => (
                  <div
                    key={tile.index}
                    className={`tile ${playerBTile?.index === tile.index ? 'selected' : ''}`}
                    onClick={() => handleBTileClick(tile)}
                  >
                    {tile.value}
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
            {playerBTiles.map((tile) => (
                <div
                  key={tile.index}
                  className={`tile ${playerBTile?.index === tile.index ? 'selected' : ''}`}
                  onClick={() => handleBTileClick(tile)}
                >
                  {tile.value}
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
