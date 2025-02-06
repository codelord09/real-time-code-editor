import React, { useState } from "react";
import CodeEditor from "./components/CodeEditor";
import LiveCollaboration from "./components/LiveCollaboration";
import AISuggestions from "./components/AISuggestions";

function App() {
  const [code, setCode] = useState("");
  const clientId = Math.floor(Math.random() * 1000); // Generate a random client ID

  return (
    <div style={{ padding: "20px" }}>
      <h1>Real-Time Collaborative Code Editor</h1>
      <CodeEditor onCodeChange={setCode} />
      <LiveCollaboration clientId={clientId} onRemoteCodeChange={setCode} />
      <AISuggestions code={code} />
    </div>
  );
}

export default App;