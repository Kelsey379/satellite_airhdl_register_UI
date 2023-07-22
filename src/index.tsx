import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import './index.css';

// Function to trigger the Python script
const generateJsonFiles = async () => {
};

// Call the function to trigger the Python script when the app loads
generateJsonFiles();

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
