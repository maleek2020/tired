import React from "react";
import "../styles/navbar.css";

const Navbar = ({ setShow, size }) => {
  return (
    <nav>
      <div className="nav_box">
        <span className="my_shop" onClick={() => setShow(true)}>
          Lifestore Healthcare
        </span>
        <div className="cart" onClick={() => setShow(false)}>
          <span>
            <img className="igm" src="../images/shopping-cart.png" alt="" />
            {/* <i className="fas fa-cart-plus"></i> */}
          </span>
          <span>{size}</span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
