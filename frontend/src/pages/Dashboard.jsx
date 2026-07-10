import React from "react";

import Header from "../components/Header";
import PlayerCard from "../components/PlayerCard";
import LyricsPanel from "../components/LyricsPanel";

const demoTrack = {
  connected: true,
  albumImage: "",
  song: "Not Playing",
  artist: "Unknown Artist",
  album: "Unknown Album",
  currentTime: "0:00",
  duration: "0:00",
  lyrics: [
    "Login successful.",
    "Waiting for Spotify playback...",
    "Once music starts, synchronized lyrics will appear here.",
  ],
};

function Dashboard() {
  return (
    <main className="dashboard">
      <Header connected={demoTrack.connected} />

      <section className="dashboard-container">
        <PlayerCard 
          albumImage={demoTrack.albumImage}
          song={demoTrack.song}
          artist={demoTrack.artist}
          album={demoTrack.album}
          currentTime={demoTrack.currentTime}
          duration={demoTrack.duration}
        />

        <LyricsPanel lyrics={demoTrack.lyrics}/>
      </section>
    </main>
  );
}

export default Dashboard;