import React from "react";
// import Filters from "../components/Filters";
import NavBar from './NavBar';

function Layout({children}){
return(
<>
 <div className="bg-maincolor text-white"></div>
 <NavBar /> 
 {children}
 {/* <Filters/> */}
 <div/>
    
</>
);
}
export default Layout ;