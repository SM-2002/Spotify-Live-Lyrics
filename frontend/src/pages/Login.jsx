import React from "react";

function Login() {
  const handleSpotifyLogin = () => {
    window.location.href = "http://127.0.0.1:8000/auth/login";
  };

  return (
    <main className="app-shell">
      <section className="player-panel" aria-label="Spotify live lyrics">
        <div className="album-art" aria-hidden="true">
          <span>♪</span>
        </div>

        <div className="track-meta">
          <p className="eyebrow">Spotify Live Lyrics</p>

          <h1>Connect Spotify</h1>

          <p className="subtitle">
            Login with your Spotify account to view your currently playing song
            and synchronized lyrics in real time.
          </p>

          <button
            type="button"
            className="login-button"
            onClick={handleSpotifyLogin}
          >
            Login with Spotify
          </button>
        </div>
      </section>
    </main>
  );
}

export default Login;