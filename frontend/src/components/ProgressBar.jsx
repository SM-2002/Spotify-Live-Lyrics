import React from "react";

function ProgressBar({ currentTime, duration }) {
  return (
    <div className="progress-section">

      <div className="progress-bar">
        <div className="progress-fill"></div>
      </div>

      <div className="time-row">
        <span>{currentTime}</span>
        <span>{duration}</span>
      </div>

    </div>
  );
}

export default ProgressBar;