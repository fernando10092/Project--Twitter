import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from 'react-redux';
import {store} from './store';



createRoot(document.getElementById('root')!).render(

  <>
    <Provider store={store}>
      <App />
    </Provider>,
  </>
)