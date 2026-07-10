import React from "react";
import ProgressBar from "./ProgressBar";

function PlayerCard({
  albumImage,
  song,
  artist,
  album,
  currentTime,
  duration,
}) {
  return (
    <div className="player-card">

      <div className="album-placeholder">
        {albumImage ? (
          <img src={albumImage} alt={song} />
        ) : (
          "♪"
        )}
      </div>

      <h2>{song}</h2>

      <p className="artist-name">{artist}</p>

      <p className="album-name">{album}</p>

      <ProgressBar
        currentTime={currentTime}
        duration={duration}
      />

    </div>
  );
}

export default PlayerCard;