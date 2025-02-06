import React, { useState } from "react";
import { Controlled as CodeMirror } from "react-codemirror2";
import "codemirror/lib/codemirror.css";
import "codemirror/theme/material.css";
import "codemirror/mode/javascript/javascript";

const CodeEditor = ({ onCodeChange }) => {
    const [code, setCode] = useState("");

    return (
        <CodeMirror
            value={code}
            options={{
                mode: "javascript",
                theme: "material",
                lineNumbers: true,
            }}
            onBeforeChange={(editor, data, value) => {
                setCode(value);
                onCodeChange(value); // Send updated code to parent
            }}
        />
    );
};

export default CodeEditor;