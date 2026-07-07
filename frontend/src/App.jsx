import React from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

function App() {
  return (
    <main className="app-shell">
      <section className="player-panel" aria-label="Spotify live lyrics">
        <div className="album-art" aria-hidden="true">
          <span>♪</span>
        </div>
        <div className="track-meta">
          <p className="eyebrow">Spotify Live Lyrics</p>
          <h1>Connect Spotify</h1>
          <p className="subtitle">Current track and synced lyrics will appear here.</p>
          <button type="button" className="login-button">
            Login with Spotify
          </button>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
