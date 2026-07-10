import React from "react";
import ConnectionStatus from "./ConnectionStatus";

function Header({ connected }) {
  return (
    <header className="dashboard-header">
      <h1>Spotify Live Lyrics</h1>

      <ConnectionStatus connected={connected} />
    </header>
  );
}

export default Header;
