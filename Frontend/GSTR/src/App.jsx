/* eslint-disable no-unused-vars */
import React from 'react';
import { Route} from 'react-router-dom';
import { Switch } from 'react-router-dom';

// import { Link } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import Services from './components/Services';
import Navbar from './components/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import Signup from './components/Signup';
import LoginPage from './components/Login';

const App = () => {
  return (
    <div>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/contact" component={Contact} />
        <Route path="/services" component={Services} />
        <Route path="/signup" component={Signup} />
        <Route path="/login" component={LoginPage} />
      </Switch>
    </div>
  );
};

export default App;




