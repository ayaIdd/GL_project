import { Listbox,Transition } from "@headlessui/react";
import React, { useState,Fragment } from "react";
import { FaCheck } from "react-icons/fa";
const ModuleData = [
  {title:"Module"},
    {title:"Physique"},
    {title:"Mathematique"},
    {title:"histoire"},
    {title:"geography"},
]

const NiveauData = [
    {title:"Niveau"},
    {title:"Primaire"},
    {title:"Secondaire"},
    {title:"lycee"},
    {title:"universitaire"},
]
const WilayaData = [
    {title:"Alger"},
    {title:"Bejaia"},
    {title:"Boumerdes"},
    {title:"Tebessa"},
    {title:"Tizi"},
]


  
  function Filters() {
   

    
    const [Module,setModule]=useState(ModuleData[0]);
    const [Niveau,setNiveau]=useState(NiveauData[0]);
    const [Wilaya,setWilaya]=useState(WilayaData[0]);

const filter=[
    {
        value:Module,
        onChange:setModule,
        items:ModuleData
    },

    {
        value:Niveau,
        onChange:setNiveau,
        items:NiveauData
    },

    {
        value:Wilaya,
        onChange:setWilaya,
        items:WilayaData
    },
]
    return(
        <div className="my-6 bg-slate-600 text-white border-gray-300 grid md:grid-cols-4 grid-cols-2 lg:gap-12 gap-2 rounded p-6">
            {
filter.map((items, index) =>(
    <Listbox key={index} value={items.value} onChange={items.onChange}>
        <div className="relative">
            <Listbox.Button className="relative border border-gray-700 w-full text-white">
            <span className="block truncate">{items.value.title}</span>
            <span className="absolute inset-y-0 flex items-center pointer-events-none ">
                <FaCheck className="h-5 w-5" aria-hidden="true"/>
            </span>
            </Listbox.Button>
            <Transition as={Fragment} leave="transition ease-in duration-100"  leavefrom="opacity-100" leaveTo="opacity-0">
            <Listbox.Options className="absolute z-10 mt-1 w-full bg-slate-400 border border-gray-300 text-black rounded-md shadow-lg max-h-60 ring-opacity-5 overflow-auto focus:outline-none sm:text-sm">
                {
                filter.items.map((iterm,i)=>(
                    <Listbox.Option key={i} className={({active}) =>
                    `relative cursor-default select-none py-2 pl-10 pr-4 ${
                        active ? "bg-slate-400 text-white":"text-maincolor"  } `}

                 value={iterm}>
                  {({selected}) =>(
                    <>
                    <span className={`block truncate ${selected ? 'font-semibold':'font-normal'}`}>
                      {iterm.title}
                    </span>{
                      selected ? (
                        <span className="absolute inset-y-0 left-0 flex items-center pl-3">
                          <FaCheck className="h-3 w-3 " aria-hidden="true"/>
                        </span>
                      ):null
                    }
                    </>
                  )}
                    </Listbox.Option>
                ))
                }
                </Listbox.Options>

            </Transition>

        </div>
        </Listbox>
    ))
}
</div>
                );
}
export default Filters;