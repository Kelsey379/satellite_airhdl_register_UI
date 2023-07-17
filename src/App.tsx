import React, { useState, useEffect } from 'react';
import { JsonForms } from '@jsonforms/react';
import { materialRenderers, materialCells } from '@jsonforms/material-renderers';
import importedSchema from './schema.json';
import importedUischema from './uischema.json'; 
import initialData from './data.json'; 

import './App.css';

function App() {
  // Retrieve data from local storage or use the initial data
  const initialData = JSON.parse(localStorage.getItem('data') || '{}');
  const [data, setData] = useState(initialData);

  // Save data to local storage whenever it changes
  useEffect(() => {
    localStorage.setItem('data', JSON.stringify(data));
  }, [data]);
  // took out 'data' state and 'onChange' handler, not needed
  return (
    <div className="App">
      <h1>PRESET AirHDL Registers</h1>
      <hr />
      <JsonForms
        schema={importedSchema}
        uischema={importedUischema}
        data={initialData}
        renderers={materialRenderers}
        cells={materialCells}
        validationMode={'ValidateAndShow'}
      />
      {/* Place the Submit button inside the last Clock_High group */}
      <div className="submit-button">
        <button type="submit">Submit</button>
      </div>
    </div>
  );
}

export default App; // Add the default export here
