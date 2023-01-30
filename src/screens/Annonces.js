import React, { useState } from "react";
// import Filters from "../components/Filters";
import Layout from "../layout/Layout";
import {Annonce1} from "../data/Annon";
import AnnonceA from "../components/AnnonceA";
import { CgSpinner } from "react-icons/cg";
import { useEffect } from "react"; 

function Annonces(){
    const maxPage= 10
    const [page,setPage] = useState(maxPage)
    const HandleLoadingMore=()=>{
        setPage(page+maxPage)
    }
    const [data, setData] = useState(null);
    useEffect(() => {
        fetch("http://localhost:8000/home/", {
            method: "GET",
            headers: { "Content-Type": "application/json" },

          })
          .then(response => response.json())
          .then(data => {
            setData(data);
            console.log(data)
          });
      }, []);

    return(
        <Layout>
         <div className="min-height-screen container mx-auto px-2 my-6">
            {/* <Filters/> */}
        </div> 
        <p className="text-lg font-medium my-6">
            Total <span className="font-bold text-maincolor">{Annonce1.length}</span>{} item found

        </p>
<div className="grid sm:mt-10 mt-6 xl:grid-cols-4 2xl:grid-cols-5 lg:grid-cols-3 sm:grid-cols-2 gap-6">
{
    Annonce1.slice(0,page)?.map((Ann,index)=>(
        <AnnonceA key={index} Ann={Ann}/>
    ))
}
  </div>
  {/* loading more */}
  <div className="w-full flex-colo md:my-20 my-10">
    <button onClick={HandleLoadingMore} className="flex-rows gap-3 text-maincolor py-3 px-8 rounded font-semibold border-2 border-maincolor">
        loading More <CgSpinner className="animate-spin"/>
    </button>
  </div>
        </Layout> );
}
export default Annonces;