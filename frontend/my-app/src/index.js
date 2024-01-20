import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './Main/Main';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ChatboxComponent from './react-components/ChatboxComponent';
import ParticleComponent from './react-components/ParticleComponent';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <React.StrictMode>
      <Routes>
        <Route exact path="/" element = {<><App/><ParticleComponent></ParticleComponent></>}/>
        <Route path="ChatboxComponent" element = {<ChatboxComponent/>}/>
      </Routes>
    </React.StrictMode>
  </Router>
);
