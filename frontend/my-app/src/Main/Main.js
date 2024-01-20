import React, { useState } from 'react';
import './Main.css';
import { Link } from 'react-router-dom';
import ChatboxComponent from '../react-components/ChatboxComponent';

function App() {
  return (
    <div className='App'>
      <link href="https://fonts.cdnfonts.com/css/arkhip" rel="stylesheet"></link>
      <header className="App-header">
        <div className="product-name">medicAI</div>
        <Link to="/ChatboxComponent" className="btn">
          CONTINUE TO PRODUCT
        </Link>
      </header>
    </div>
  );
}

export default App;
