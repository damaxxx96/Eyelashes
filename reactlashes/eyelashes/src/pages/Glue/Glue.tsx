import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Glue.css";

const GluePage: React.FC = () => {
  const [glues, setGlues] = useState<any[]>([]);

  const fetchGlues = async () => {
    try {
      const response = await axios.get("http://localhost:8000/glue/gluelist/");
      setGlues(response.data);
    } catch (error) {
      console.error("Error fetching glue:", error);
    }
  };

  useEffect(() => {
    fetchGlues();
  }, []);

  const handleAdd = async (id: number) => {
    try {
      await axios.patch(`http://localhost:8000/glue/add_glue/${id}`);
      fetchGlues(); // Fetch glues after adding
    } catch (error) {
      console.error("Error adding glue:", error);
    }
  };

  const handleSubtract = async (id: number) => {
    try {
      await axios.patch(`http://localhost:8000/glue/subtract_glue/${id}`);
      fetchGlues(); // Fetch glues after subtracting
    } catch (error) {
      console.error(`Error subtracting glue with ID ${id}:`, error);
    }
  };

  return (
    <div>
      <h2>You are at Glue</h2>
      <h3>Glue List:</h3>
      <div className="glue-list">
        {glues.map((glue: any, index: number) => {
          const glueId = glue.id !== undefined ? glue.id : index + 1; // Use index + 1 as the ID if glue.id is undefined
          return (
            <div className="glue-item" key={glueId}>
              <span>Modelname: {glue.modelname}</span>{" "}
              <span>Content: {glue.content}</span>{" "}
              <span>Count: {glue.count}</span>
              <button className="add" onClick={() => handleAdd(glueId)}>
                +
              </button>
              {glue.count > 0 && (
                <button className="sub" onClick={() => handleSubtract(glueId)}>
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

export default GluePage;
