import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Eyelashes.css";
const EyelashesPage: React.FC = () => {
  const [lashes, setLashes] = useState<any[]>([]);

  const fetchLashes = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/lashes/lasheslist"
      );

      setLashes(response.data);
    } catch (error) {
      console.error("Error fetching lashes:", error);
    }
  };

  useEffect(() => {
    fetchLashes(); // Call fetchLashes when component mounts
  }, []);

  const handleAdd = async (id: number) => {
    try {
      await axios.patch(`http://localhost:8000/lashes/add_lashes/${id}`);
      fetchLashes(); // Fetch lashes after adding
    } catch (error) {
      console.error("Error adding lashes:", error);
    }
  };

  const handleSubtract = async (id: number) => {
    try {
      await axios.patch(`http://localhost:8000/lashes/subtract_lashes/${id}`);
      fetchLashes(); // Fetch lashes after subtracting
    } catch (error) {
      console.error(`Error subtracting lashes with ID ${id}:`, error);
    }
  };

  return (
    <div>
      <h2>You are at Eyelashes</h2>
      <h3>Lashes List:</h3>
      <div className="eyelashes-list">
        {lashes.map((lash: any, index: number) => {
          const lashId = lash.id !== undefined ? lash.id : index + 1; // Use index + 1 as the ID if lash.id is undefined
          return (
            <div key={lashId} className="eyelashes-item">
              <span>Modelname: {lash.modelname}</span>{" "}
              <span>Length: {lash.length}</span>{" "}
              <span>
                Width:
                {lash.width}
              </span>
              <span>Count: {lash.count}</span>
              {lash.count > 0 && (
                <button className="sub" onClick={() => handleSubtract(lashId)}>
                  -
                </button>
              )}
              <button className="add" onClick={() => handleAdd(lashId)}>
                +
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default EyelashesPage;
