import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/Home";
import "./App.css";

const App: React.FC = () => {
  const [user, setUser] = useState<string>("");

  return (
    <div className="app">
      <Router>
        <Routes>
          <Route path="/" element={<Home user={user} />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;
