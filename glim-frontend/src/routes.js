import React from 'react'; 
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Header from './components/Header';
import Footer from './components/Footer';

import Home from './pages/Home';
import Historia from './pages/Historia';
import Time from './pages/Time';
import FAQ from './pages/FAQ';
import Buscador from './pages/Buscador'

function RoutesApp(){
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/historia" element={<Historia />} />
        <Route path="/time" element={<Time />} />
        <Route path="/faq" element={<FAQ />} />
        <Route path="/buscador" element={<Buscador />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  )
}

export default RoutesApp;