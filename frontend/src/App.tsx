import { useEffect, useState } from "react";
import { getHealth } from "./api";


function App() {

  const [backendStatus, setBackendStatus] =
    useState("Checking...");


  useEffect(() => {

    getHealth()
      .then(() => {
        setBackendStatus("Online");
      })
      .catch(() => {
        setBackendStatus("Offline");
      });

  }, []);


  return (
    <div>

      <h1>AI Trading Platform</h1>

      <p>
        AI-powered multi-asset research
        and paper trading platform.
      </p>

      <hr />

      <h2>System Status</h2>

      <p>
        Backend: {backendStatus}
      </p>

      <p>
        Market Data: Not Connected
      </p>

      <p>
        ML Model: Not Trained
      </p>

      <p>
        Trading Mode: Research
      </p>

    </div>
  );
}


export default App;