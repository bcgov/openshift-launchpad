import React, { Component } from "react";

// Component for handling Google Sign-in actions.
// Remove if not using Google Sign-in
export class GoogleLoginButton extends Component {
  componentDidMount() {
    window.onSignIn = this.onSuccess;
  }

  signOut = () => {
    const auth2 = window.gapi.auth2.getAuthInstance();
    auth2.signOut().then(() => {
      this.props.setAuthenticationStatus(false);
    });
  };

  onSuccess = googleUser => {
    // For more infomation:
    // https://developers.google.com/identity/sign-in/web/sign-in
    this.props.setAuthenticationStatus(true);
    const idToken = googleUser.getAuthResponse().id_token;
    this.props.setIdToken(idToken);
  };

  render() {
    return (
      <div>
        <button
          style={{
            height: "36px",
            width: "120px",
            cursor: "pointer",
            float: "right",
            display: this.props.isAuthenticated ? "block" : "none",
          }}
          onClick={this.signOut}
        >
          Sign Out
        </button>
        <div
          style={{
            float: "right",
            display: this.props.isAuthenticated ? "none" : "block",
          }}
          className="g-signin2"
          data-onsuccess="onSignIn"
        />
      </div>
    );
  }
}

export default GoogleLoginButton;
