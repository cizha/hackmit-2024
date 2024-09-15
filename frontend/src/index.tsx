import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App';
import Game from './game';

const Root: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/scrabble" element={<Game />} />
      </Routes>
    </Router>
  );
};

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement!);  // React 18 uses createRoot
root.render(<Root />);

// // allows for live updating
// module.hot.accept();

