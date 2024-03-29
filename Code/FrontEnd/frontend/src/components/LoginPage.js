import React, { useState } from 'react';
import Parse from 'parse/dist/parse.min.js';
import './App.css';
import { Button, Divider, Input } from 'antd';

export const UserLogin = () => {
  // State variables
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [currentUser, setCurrentUser] = useState(null);

  // Function that will return current user and also update current username
  const getCurrentUser = async function () {
    const currentUser = await Parse.User.current();
    // Update state variable holding current user
    setCurrentUser(currentUser);
    return currentUser;
  };

  return (
    <div>
      <div className="header">
        <img
          className="header_logo"
          alt="Back4App Logo"
          src={
            'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
          }
        />
        <p className="header_text_bold">{'React on Back4App'}</p>
        <p className="header_text">{'User Login'}</p>
      </div>
      <div className="container">
        <h2 className="heading">{'User Login'}</h2>
        <Divider />
        <div className="form_wrapper">
          <Input
            value={username}
            onChange={(event) => setUsername(event.target.value)}
            placeholder="Username"
            size="large"
            className="form_input"
          />
          <Input
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Password"
            size="large"
            type="password"
            className="form_input"
          />
        </div>
        <div className="form_buttons">
          <Button
            onClick={() => doUserLogIn()}
            type="primary"
            className="form_button"
            color={'#208AEC'}
            size="large"
            block
          >
            Log In
          </Button>
        </div>
        <Divider />
        <div className="login-social">
          <div className="login-social-item login-social-item--facebook">
            <img className="login-social-item__image" src={'https://findicons.com/files/icons/2830/clean_social_icons/250/facebook.png'} alt=""/>
          </div>
          <div className="login-social-item">
            <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
          </div>
          <div className="login-social-item">
            <img className="login-social-item__image" src={'data:image/png;base64,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'} alt=""/>
          </div>
        </div>
        <p className="form__hint">Don't have an account? <a className="form__link" href="#">Sign up</a></p>
      </div>
    </div>
  );
};