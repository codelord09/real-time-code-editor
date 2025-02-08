import React, { useState } from "react";
import axios from "axios";

const AISuggestions = ({ code }) => {
    const [suggestions, setSuggestions] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const getDebuggingSuggestions = async () => {
        // Reset states before making a new request
        setSuggestions("");
        setError("");
        setLoading(true);

        try {
            console.log("Sending request with code:", { code });

            // Send POST request to the backend
            const response = await axios.post(
                "http://localhost:8000/debug/",
                { code }, // Send code in the body as an object
                {
                    headers: {
                        "Content-Type": "application/json", // Ensure the content type is set
                    },
                }
            );

            console.log("Response from server:", response.data);

            // Update state with AI suggestions
            setSuggestions(response.data.suggestions || "No suggestions available.");
        } catch (err) {
            console.error("Error fetching AI suggestions:", err);

            // Handle errors gracefully
            if (err.response) {
                setError(`Server Error: ${err.response.status} - ${err.response.data.error || "Unknown error"}`);
            } else if (err.request) {
                setError("No response received from the server. Please check your connection.");
            } else {
                setError(`Error: ${err.message}`);
            }
        } finally {
            setLoading(false); // Stop loading regardless of success or failure
        }
    };

    return (
        <div style={{ marginTop: "20px" }}>
            {/* Button to trigger AI suggestions */}
            <button onClick={getDebuggingSuggestions} disabled={loading}>
                {loading ? "Fetching Suggestions..." : "Get AI Suggestions"}
            </button>

            {/* Display loading state */}
            {loading && <p>Loading...</p>}

            {/* Display error message if any */}
            {error && <p style={{ color: "red" }}>{error}</p>}

            {/* Display AI suggestions */}
            {suggestions && (
                <div>
                    <h3>AI Suggestions:</h3>
                    <pre>{suggestions}</pre>
                </div>
            )}
        </div>
    );
};

export default AISuggestions;