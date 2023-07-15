import React, { useState } from 'react';
import { JsonForms } from '@jsonforms/react';
import { materialRenderers, materialCells } from '@jsonforms/material-renderers';
import importedSchema from './schema.json';
import importedUischema from './uischema.json'; 
import initialData from './data.json'; 

import './App.css';

function App() {
  const [data, setData] = useState(initialData);

  return (
    <div className="App">
      <h1>PRESET AirHDL Registers</h1>
      <hr/>
      <JsonForms
        schema={importedSchema}
        uischema={importedUischema}
        data={data}
        renderers={materialRenderers}
        cells={materialCells}
        onChange={({ data, errors }) => setData(data)}
      />
      <div className="submit-button">
        <button type="submit">Submit</button>
      </div>
    </div>
    
  );
}

export default App;
