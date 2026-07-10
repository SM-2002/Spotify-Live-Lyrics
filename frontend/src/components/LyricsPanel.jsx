import React from "react";

function LyricsPanel({ lyrics }) {
  return (
    <div className="lyrics-card">

      <h2>Lyrics</h2>

      <div className="lyrics-placeholder">

        {lyrics.map((line, index) => (
          <p key={index}>{line}</p>
        ))}

      </div>

    </div>
  );
}

export default LyricsPanel;