import React, { useEffect } from "react";
import io from "socket.io-client";

// Connect to a socket.io server, passing an array of URLs if necessary
const socket = io("http://localhost:3000"); // Use one URL or an array of URLs if needed

const LiveCollaboration = ({ clientId, onRemoteCodeChange }) => {
  useEffect(() => {
    // Join the session
    socket.emit("join", `Client #${clientId}`);

    // Listen for messages
    socket.on("receive_message", (data) => {
      console.log("Received message:", data);
      if (!data.includes(`Client #${clientId}`)) {
        onRemoteCodeChange(data.split(" says: ")[1]);
      }
    });

    // Cleanup on unmount
    return () => {
      socket.disconnect();
    };
  }, [clientId, onRemoteCodeChange]);

  const sendMessage = () => {
    socket.emit("send_message", `Hello from Client #${clientId}`);
  };

  return (
    <div>
      <button onClick={sendMessage}>Send Message</button>
      <p>Live Collaboration Active</p>
    </div>
  );
};

export default LiveCollaboration;
