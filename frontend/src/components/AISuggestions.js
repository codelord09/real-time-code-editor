import React, { useState } from "react";
import axios from "axios";

const AISuggestions = ({ code }) => {
    const [suggestions, setSuggestions] = useState("");

    const getDebuggingSuggestions = async () => {
        try {
            const response = await axios.post("http://localhost:8000/debug/", { code });
            setSuggestions(response.data.suggestions);
        } catch (error) {
            console.error("Error fetching AI suggestions:", error);
        }
    };

    return (
        <div>
            <button onClick={getDebuggingSuggestions}>Get AI Suggestions</button>
            <pre>{suggestions}</pre>
        </div>
    );
};

export default AISuggestions;