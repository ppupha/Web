import logo from './logo.svg';
import './App.css';
//import './static/css/style.css'
//import './static/css/style.css'

import PlaceList from './components/placeList'
import HomePage from './components/homePage'
import PlaceListPage from './components/placeListPage'
import PlacePage from './components/placePage'
import ProfilePage from './components/profilePage'
import Test from './components/Test.js'

import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect,
    useParams} from "react-router-dom";


function requireAuth(nextState, replace, next) {
  if (!this.authenticated) {
    replace({
      pathname: "/login",
      state: {nextPathname: nextState.location.pathname}
    });
  }
  next();
}

class App extends React.Component {
  render(){
    return (
      <>
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/placeList/:type" component={PlaceListPage} onEnter={requireAuth} />
          <Route exact path="/profile/" component={ProfilePage} />

          <Route exact path="/test/" component={Test} />
          <Route path="/place/:id" component={PlacePage} />
          {/*<Route path="/about" component={About} /> */}

          {/*
          <Route path="/contactus" component={ContactUs} />
          */}

          {/* If any route mismatches the upper
          route endpoints then, redirect triggers
          and redirects app to home component with to="/" */}
          <Redirect to="/" />
        </Switch>
      </Router>
    </>
  );
  }

}

export default App;
