/* eslint-disable react-refresh/only-export-components */
/* eslint-disable no-unused-vars */
import React from "react";
import { createRoot } from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
  Routes,
  Route,
  Link,
} from "react-router-dom";
import Home from './components/Home';
import About from './components/About'
import Contact from "./components/Contact";
import Services from "./components/Services";
import Navbar from "./components/Navbar";
import Signup from "./components/Signup";
import LoginPage from "./components/LoginPage"
import 'bootstrap/dist/css/bootstrap.min.css';
import "./CSS/style.css"





const App = () => {
  return (
    <div className="engulf">
      <Navbar />
      <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/services" element={<Services />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/loginPage" element={<LoginPage />} />
      </Routes>
    </div>
  );
}

const router = createBrowserRouter([

  {
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />,

      },
      {
        path: "about",
        element: <About />,
      },
      {
        path: "contact",
        element: <Contact />,
      },
      {
        path: "services",
        element: <Services />,
      },
      {
        path: "signup",
        element: <Signup />,
      },
      {
        path: "loginPage",
        element: <LoginPage />,
      },
    ]
  }


]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);

