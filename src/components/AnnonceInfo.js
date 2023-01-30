import React from "react";


function AnnonceInfo({Ann}){

    return(
        <div className="w-full xl:h-screen relative text-black">
        
        <img src={`${Ann?.image}`}
        alt={Ann.name}
        className="w-full hidden xl:inline-block h-full object-cover" />
        
        <div className="xl:bg-pink bg-white flex-colo xl:bg-opacity-70 xl:absolute top-0 left-0 right-0 bottom-0">
        <div className="container px-3 mx-auto 2xl:px-32 xl:grid grid-cols-3 flex-colo py-10 lg:py-20 gap-8">
          <div className="xl:col-span-1 w-full xl:order-none order-last h-full bg-pink-400 border border-maincolor rounded-none-lg overflow-hidden"> 
          <img src={`${Ann?.image}`}
    
          alt={Ann.name}
          className="w-full object-cover "/>
        </div>
        <div className="col-span-2 md:grid grid-cols-5 gap-4 items-center">
            <div className="col-span-3 flex flex-col gap-10">
                <h1 className="xl:text-4xl capitalize font-sans text-2xl font bold">
                    {Ann?.name}
                </h1>

            </div>
            <p className="text-black text-sm leading">{Ann?.desc}</p>
           
            <div className="col-span-2 flex-colo font-medium text-sm">
                <p>
                    Le Niveau:{" "}
                     <span className="ml-2 truncate">{Ann?.Niveau}</span>
                </p>
            </div>

            <div className="col-span-2 flex-colo font-medium text-sm">
                <p>
                    Le Module:{" "}
                     <span className="ml-2 truncate">{Ann?.Module}</span>
                </p>
            </div>

            <div className="col-span-2 flex-colo font-medium text-sm">
                <p>
                    La Wilaya:{" "}
                     <span className="ml-2 truncate">{Ann?.Wilaya}</span>
                </p>
            </div>
            <div className="col-span-2 flex-colo font-medium text-sm">
                <p>
                    Le Prix:{" "}
                     <span className="ml-2 truncate">{Ann?.Prix}</span>
                </p>
            </div>

        </div>
        </div>
        </div>
        </div>
    );
}
export default AnnonceInfo;