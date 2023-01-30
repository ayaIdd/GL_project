import React from "react";
import { Route, Routes } from "react-router-dom";
import Homescreen from "./screens/Homescreen";
import Details from "./screens/Details";
import Login from "./screens/Login";
import Annonces from "./screens/Annonces";



function App() {                           
  return (
    <Routes>
      <Route path="/" element={<Homescreen/>}/>
      <Route path="/Annonces/:id" element={<Details />}/>
      <Route path="/Annonces" element={<Annonces />}/>
      <Route path="/login" element={<Login/>}/>
      
      
    </Routes>

  );
}
export default App;
