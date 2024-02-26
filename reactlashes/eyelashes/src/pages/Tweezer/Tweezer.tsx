import React, { useState, useEffect } from "react";
import axios from "axios";
import { TweezerService } from "../../services/TweezerService";
import "./Tweezer.css";

const TweezersPage: React.FC = () => {
  const [tweezers, setTweezers] = useState<any[]>([]);

  const fetchTweezers = async () => {
    const response = await TweezerService.fetchTweezers();
    setTweezers(response);
  };

  useEffect(() => {
    fetchTweezers();
  }, []); // Empty dependency array to run the effect only once after the initial render

  const handleAdd = async (id: number) => {
    try {
      await axios.patch(`http://localhost:8000/tweezer/add_tweezer/${id}`);
      fetchTweezers(); // Fetch tweezers after adding
    } catch (error) {
      console.error("Error adding tweezer:", error);
    }
  };

  const handleSubtract = async (id: number) => {
    try {
      await axios.patch(`http://localhost:8000/tweezer/subtract_tweezer/${id}`);
      fetchTweezers(); // Fetch tweezers after subtracting
    } catch (error) {
      console.error(`Error subtracting tweezer with ID ${id}:`, error);
    }
  };

  return (
    <div>
      <h2>You are at Tweezers</h2>
      <h3>Tweezers List:</h3>
      <div className="tweezer-list">
        {tweezers.map((tweezer: any, index: number) => {
          const tweezerId = tweezer.id !== undefined ? tweezer.id : index + 1; // Use index + 1 as the ID if tweezer.id is undefined
          return (
            <div className="tweezer-item" key={tweezerId}>
              <span>Modelname: {tweezer.modelname}</span>
              <span> Color: {tweezer.color}</span>{" "}
              <span>Count: {tweezer.count}</span>
              <button className="add" onClick={() => handleAdd(tweezerId)}>
                +
              </button>
              {tweezer.count > 0 && (
                <button
                  className="sub"
                  onClick={() => handleSubtract(tweezerId)}
                >
                  -
                </button>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default TweezersPage;
