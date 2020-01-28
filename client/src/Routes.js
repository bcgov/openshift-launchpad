import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "@/components/Home";
import AboutUs from "@/components/AboutUs";
import NotFound from "@/components/NotFound";
import Login from "@/components/Login";

const PublicRoutes = () => (
  <Switch>
    <Route component={Login} />
  </Switch>
);

const PrivateRoutes = () => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route exact path="/about-us" component={AboutUs} />
    <Route component={NotFound} />
  </Switch>
);

export { PublicRoutes, PrivateRoutes };
