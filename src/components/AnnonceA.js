import React from "react";
import {Link} from "react-router-dom";
// import { FaHeart } from "react-icons/fa";


function AnnonceA({Ann}){
    return(
        <>
        <div className="border border-maincolor p1 hover:scale-95 transition relative">
            <Link to={`${Ann?.name}`} className="w-full">
                <img 
            src={`${Ann?.image}`}
            alt={Ann?.name}
            className="w-full h-64 object-cover"/>
            
</Link>
<div className="absolute flex-btn gap-2 bottom-0 right-0 left-0 bg-maincolor">
    <h3 className="font-semibold text-white truncate pl-3">{Ann?.name}</h3>
    <button className="h-9 w-9 text-sm flex-colo  ">
    {/* <FaHeart className="w-6 h-6 " /> */}
    </button>
</div>

        </div>
        </>
    )
}

    export default AnnonceA;