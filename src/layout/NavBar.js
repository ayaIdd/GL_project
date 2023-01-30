import React from "react";
import {Link, NavLink } from "react-router-dom";
import{GoSearch} from "react-icons/go";
import{CgUser} from "react-icons/cg";
import{FaHeart} from "react-icons/fa";

function NavBar(){
    const hover = 'hover:text-white transitions text-black';
    const Hover=({isActive})=>(isActive ? 'text-white':hover);
return (
    <>
    <div className="bg-white shadow-md sticky top-0 z-20">
       
     <div className="container bg-maincolor mx-auto py-6 px-2 lg:grid gap-10 grid-cols-7 justify-between items-center">
       <div className="col-span-1 lg:block hidden">
        <Link to="/">
            <img
             src="logo1.png"
             alt="logo" 
             className="w-full h-12 object-contain"
            />
            
        </Link>
       </div>
       <div className="col-span-3">
        <form className="w-full text-sm bg-white rounded flex-btn gap-4">
        <button type="submit" className="bg-white w-12 flex-colo h-12 rounded text-black">
        <GoSearch />
        </button>
        <input type="text" placeholder="search any annonce from here"
        className="font-medium placeholder:text-black text-sm w-11/12 h-12 bg-transparent border-none px-2 text-black"
        />

        
        </form>
       </div>
       <div className="col-span-3 font-medium text-sm hidden xl:gap-14 2xl:gap-20 justify-between lg:flex xl:justify-end items-center ">
        <NavLink to="/Annonces" className={Hover}>
            Annonces
        </NavLink>
        <NavLink to="/ContactUs" className={Hover}>
        ContactUs
        </NavLink>
        <NavLink to="/Login" className={Hover}>
            <CgUser className="w-8 h-8" />
        </NavLink>
        <NavLink to="/Favorites" className={Hover}>
        <FaHeart className="w-6 h-6" />
        </NavLink>

       </div>
     </div>
    </div>
    </>
);

}
export default NavBar;