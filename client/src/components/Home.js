import React from "react";
import { Link } from "react-router-dom";

const Home = props => (
  <div>
    <h1>Basic React App</h1>
    {props.name && <p>Hello, {props.name}!</p>}
    <Link to="/about-us">Go to About Us</Link>
  </div>
);

export default Home;
