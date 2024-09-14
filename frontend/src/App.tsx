import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const gridSize = 15 * 15;
  const [selectedCell, setSelectedCell] = useState<number | null>(null);
  const [grid, setGrid] = useState<string[]>(Array(gridSize).fill(""));

  const handleCellClick = (index: number) => {
    setSelectedCell(index);
  };

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    if (selectedCell !== null && /^[0-9]$/.test(value)) {
      const updatedGrid = [...grid];
      updatedGrid[selectedCell] = value;
      setGrid(updatedGrid);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <p>SCRABBLE</p>
      </div>
      <div className="grid-board">
        {grid.map((cellValue, index) => (
          <div
            key={index}
            className={`grid-item ${selectedCell === index ? 'selected' : ''}`}
            onClick={() => handleCellClick(index)}
          >
            {cellValue || index + 1}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input 
          type="text" 
          onChange={handleInputChange} 
          maxLength={1}
          placeholder="Type a number"
        />
      </div>
    </div>
  );
};

export default App;
