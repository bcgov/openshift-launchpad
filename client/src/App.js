import React, { Component } from "react";
import { BrowserRouter } from "react-router-dom";
import { PublicRoutes, PrivateRoutes } from "@/Routes";
import "@/styles/index.scss";

import { GoogleLoginButton } from "@/components/GoogleLoginButton";

// Toggle on Google Sign-in
// NOTE: Hot module replacement causes the button to disappear.
//       This is not a problem when the app is built "normally."
//       Refresh the browser to see the button again.
const USE_GOOGLE_SIGNIN = false;

const App = !USE_GOOGLE_SIGNIN
  ? // Simple Stateless component
    () => (
      <BrowserRouter>
        <PrivateRoutes />
      </BrowserRouter>
    )
  : // Stateful component for Google Sign-in support
    // Remove if not using Google Sign-in
    class App extends Component {
      state = { isAuthenticated: false, authComplete: false, idToken: null };

      componentDidMount() {
        if (process.env.GOOGLE_SIGNIN_CLIENT === "") {
          console.error("Please add a valid GOOGLE_SIGNIN_CLIENT to .env");
          return;
        }
        this.setupGoogleLogin();
      }

      setupGoogleLogin = () => {
        window.gapi.load("auth2", () => {
          const auth2 = window.gapi.auth2.init({
            client_id: process.env.GOOGLE_SIGNIN_CLIENT,
          });
          this.handleAuthState(auth2.isSignedIn.get());
          auth2.isSignedIn.listen(this.handleAuthState);
        });
      };

      handleAuthState = value => {
        // Abort subsequent invocations once authenticated
        if (this.state.authComplete) {
          return;
        }

        const authStatus =
          value === undefined ? this.state.authStatus || false : value;
        this.setState({
          isAuthenticated: authStatus,
          authComplete: true,
          authStatus: value,
        });
      };

      renderRoutes = () =>
        this.state.isAuthenticated ? <PrivateRoutes /> : <PublicRoutes />;

      render() {
        return (
          <div>
            <GoogleLoginButton
              setAuthenticationStatus={isAuthenticated =>
                this.setState({ isAuthenticated })
              }
              setIdToken={idToken => this.setState({ idToken })}
              isAuthenticated={this.state.isAuthenticated}
            />
            <BrowserRouter>{this.renderRoutes()}</BrowserRouter>
          </div>
        );
      }
    };

export default App;
