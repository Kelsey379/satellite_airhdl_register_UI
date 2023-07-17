import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // Correct import path

import './index.css';

// Function to trigger the Python script
const generateJsonFiles = async () => {
  // ... (rest of the code remains the same)
};

// Call the function to trigger the Python script when the app loads
generateJsonFiles();

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
