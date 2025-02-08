import React, { useState } from "react";
import CodeEditor from "./components/CodeEditor";
import LiveCollaboration from "./components/LiveCollaboration";
import AISuggestions from "./components/AISuggestions";

function App() {
  const [code, setCode] = useState(""); // State for the current code
  const [remoteCode, setRemoteCode] = useState(""); // State for code changes from collaborators
  const clientId = Math.floor(Math.random() * 1000); // Generate a random client ID

  // Function to handle local code changes
  const handleCodeChange = (newCode) => {
    setCode(newCode);
  };

  // Function to handle remote code changes (from collaborators)
  const handleRemoteCodeChange = (newCode) => {
    setRemoteCode(newCode);
    setCode(newCode); // Sync local code with remote changes
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Real-Time Collaborative Code Editor</h1>

      {/* Code Editor */}
      <CodeEditor
        code={remoteCode || code} // Use remote code if available, otherwise use local code
        onCodeChange={handleCodeChange}
      />

      {/* Real-Time Collaboration */}
      <LiveCollaboration
        clientId={clientId}
        onRemoteCodeChange={handleRemoteCodeChange}
      />

      {/* AI Suggestions */}
      <AISuggestions code={code} />
    </div>
  );
}

export default App;