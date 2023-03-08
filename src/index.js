import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./Layout";
import Home from "./pages/Home";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import LandingPage from "./pages/LandingPage";
import Profile from "./pages/Profile";
import QRcode from "./pages/QRcode";
import Survey from "./pages/Survey";
import Thanks from "./pages/Thanks";
//import dbtest from "./pages/dbtest";
import './main.css';

/*
import { Amplify } from 'aws-amplify';
import config from './aws-exports';
Amplify.configure(config);*/

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="Signup" element={<Signup />} />
          <Route path="Login" element={<Login />} />
          <Route path="LandingPage" element={<LandingPage />} />
          <Route path="Profile" element={<Profile />} />
          <Route path="QRcode" element={<QRcode />} />
          <Route path="Survey" element={<Survey />} />
          <Route path="Thanks" element={<Thanks />} />
          {/* <Route path="dbtest" element={<dbtest />} /> */}
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
