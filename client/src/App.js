import React from 'react';
import { BrowserRouter } from 'react-router-dom';

import PublicRoutes from '@/Routes';
import '@/styles/index.scss';

const App = () => (
  <BrowserRouter>
    <PublicRoutes />
  </BrowserRouter>
);

export default App;
