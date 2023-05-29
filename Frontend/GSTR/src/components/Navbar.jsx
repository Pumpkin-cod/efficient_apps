/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { NavLink } from 'react-router-dom';
import { FaBars, FaTimes } from 'react-icons/fa';
import { IconContext } from 'react-icons/lib';

function Navbar() {
    const [click, setClick] = useState(false);
    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    return (
        <div>
            <IconContext.Provider value={{ color: "#fff" }}>
                <nav className='navbar'>
                    <div className='navbar-container container'>
                        <div className='navbar-logo'>
                            <Link to="/" onClick={closeMobileMenu}>
                                <img src='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpbs.twimg.com%2Fprofile_images%2F1458078161556541443%2F-l-c3MB6.jpg&f=1&nofb=1&ipt=3da83356342e608e3ec7909aaa14cba79c6662d1af2699bc475150766a986ab7&ipo=images' />
                                {/* <h4>EFFICIENT 
                                <br />
                                CORPORATES</h4> */}
                            </Link>
                        </div>
                        <div className='menu-icon' onClick={handleClick}>
                            {click ? <FaTimes /> : <FaBars />}
                        </div>
                        <ul className={click ? "nav-menu active" : "nav-menu"}>
                            <li className='nav-item'>
                                <NavLink to="/" className={({ isActive }) => "nav-links" + (isActive ? " activated" : "")} onClick={closeMobileMenu}>Home</NavLink>
                            </li>
                            <li className='nav-item'>
                                <NavLink to="/about" className={({ isActive }) => "nav-links" + (isActive ? " activated" : "")} onClick={closeMobileMenu}>About</NavLink>
                            </li>
                            <li className='nav-item'>
                                <NavLink to="/contact" className={({ isActive }) => "nav-links" + (isActive ? " activated" : "")} onClick={closeMobileMenu}>Contact</NavLink>
                            </li>
                            <li className='nav-item'>
                                <NavLink to="/services" className={({ isActive }) => "nav-links" + (isActive ? " activated" : "")} onClick={closeMobileMenu}>Services</NavLink>
                            </li>
                        </ul>
                        <ul className={click ? "nav-menu active" : "nav-menu"}>
                            <li className='nav-item signup' >
                                <NavLink to="/signup" className={({ isActive }) => "nav-links" + (isActive ? " activated" : "")} onClick={closeMobileMenu}>Sign Up</NavLink>
                            </li>
                            <li className='nav-item'>
                                <NavLink to="/loginPage" className={({ isActive }) => "nav-links" + (isActive ? " activated" : "")} onClick={closeMobileMenu}>Login</NavLink>
                            </li>
                        </ul>
                    </div>
                </nav>
            </IconContext.Provider>
        </div>
    );
}

export default Navbar;
