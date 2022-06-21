import React from "react";
import list from "../data";
import Cards from "./card";
import "../styles/lifestore.css";

const Lifestore = ({ handleClick }) => {
  return (
    <section className="">
      {list.map((item) => (
        <Cards key={item.sku} item={item} handleClick={handleClick} />
      ))}
    </section>
  );
};

export default Lifestore;
