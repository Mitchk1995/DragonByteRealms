// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import Characters from './components/Characters';

const App = () => {
  const [token, setToken] = useState('');

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/register">Register</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/characters">Characters</Link></li>
          </ul>
        </nav>
        <Switch>
          <Route path="/register" component={Register} />
          <Route path="/login" render={(props) => <Login setToken={setToken} {...props} />} />
          <Route path="/characters" render={(props) => <Characters token={token} {...props} />} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
