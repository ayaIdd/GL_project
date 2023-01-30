import React from "react";
import Layout from "../layout/Layout";
import Annonces from "./Annonces";
// import Filters from "../components/filters";
function Homescreen(){
    return(
    <Layout>
          <Annonces/>  
    </Layout>
    );
}
export default Homescreen;