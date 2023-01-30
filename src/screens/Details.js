import React from "react";
import { useParams } from "react-router-dom";
import { Annonce1 } from "../data/Annon";
import Layout from "../layout/Layout";
import AnnonceInfo from "../components/AnnonceInfo";
function Details(){
    const id=useParams().id;
    const Ann = Annonce1.find((Ann) => Ann.name === id);
    return(
      <Layout>
     <AnnonceInfo Ann={Ann} />
      </Layout>
    );
}
export default Details;