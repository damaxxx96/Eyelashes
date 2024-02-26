import React, { useState } from "react";
import { Link } from "react-router-dom";
import logo from "../../assets/eye.jpg";
import GluePage from "../Glue/Glue";
import TweezerPage from "../Tweezer/Tweezer";
import Eyelashes from "../Eyelashes/Eyelashes";
import "./Home.css";

interface HomeProps {
  user: string;
}

const Home: React.FC<HomeProps> = ({ user }) => {
  const [showGluePage, setShowGluePage] = useState<boolean>(false);
  const [showTweezerPage, setShowTweezerPage] = useState<boolean>(false);
  const [showEyelashesPage, setShowEyelashesPage] = useState<boolean>(false);

  const toggleGluePage = () => {
    setShowGluePage((prev) => !prev);
    setShowTweezerPage(false);
    setShowEyelashesPage(false);
  };

  const toggleTweezerPage = () => {
    setShowTweezerPage((prev) => !prev);
    setShowGluePage(false);
    setShowEyelashesPage(false);
  };

  const toggleEyelashesPage = () => {
    setShowEyelashesPage((prev) => !prev);
    setShowGluePage(false);
    setShowTweezerPage(false);
  };

  return (
    <div className="home">
      <div className="navbar">
        <div className="button-container">
          <img src={logo} className="logo" alt="Logo" />
          <div className="buttons">
            <button className="oni" onClick={toggleGluePage}>
              Glue
            </button>
            <button className="oni" onClick={toggleTweezerPage}>
              Tweezer
            </button>
            <button className="oni" onClick={toggleEyelashesPage}>
              Eyelashes
            </button>
          </div>
        </div>
        {user === "" ? (
          <Link to="/login">
            <button className="loginbutton">Login</button>
          </Link>
        ) : (
          user && (
            <>
              <Link to="/admin">
                <button>Admin</button>
              </Link>
              <span> {user}</span>
            </>
          )
        )}
      </div>

      <div className="subpage">
        {/* Conditionally render GluePage */}
        {showGluePage && <GluePage />}

        {/* Conditionally render TweezerPage */}
        {showTweezerPage && <TweezerPage />}

        {/* Conditionally render EyelashesPage */}
        {showEyelashesPage && <Eyelashes />}
      </div>
    </div>
  );
};

export default Home;
