import React, { useState, useEffect } from 'react';
import axios from 'axios'

import logo from './logo.svg';
import './App.css';

function App() {

  const [musicians, setMusicians] = useState([])

  useEffect(()=> {

    axios.get('/api/musicians.json')
      .then((resp) => {
        console.log("Api Response", resp.data)
        setMusicians(resp.data)
      })

  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <ul>
          {
            musicians.map((musician, index) => {
              return <li key={index}>{musician.first_name} {musician.last_name}</li>
            })
          }

        </ul>
      </header>
    </div>
  );
}

export default App;
