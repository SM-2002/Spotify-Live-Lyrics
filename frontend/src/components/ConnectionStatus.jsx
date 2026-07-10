import React from "react";

function ConnectionStatus({ connected }) {
  return (
    <div className="connection-status">
      {connected ? "🟢 Connected" : "🔴 Disconnected"}
    </div>
  );
}

export default ConnectionStatus;