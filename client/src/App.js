import React, { Component } from "react";
import { BrowserRouter } from "react-router-dom";
import { PublicRoutes, PrivateRoutes } from "@/Routes";
import "@/styles/index.scss";

const App = () => (
  <BrowserRouter>
    <PrivateRoutes />
  </BrowserRouter>
);

export default App;
