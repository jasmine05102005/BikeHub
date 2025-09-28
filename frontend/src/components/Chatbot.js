import React, { useState, useEffect } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { text: "Hi! I am your vehicle service assistant.", sender: "bot" }
  ]);
  const [input, setInput] = useState("");
  const [userId, setUserId] = useState("");

  // Generate random userId on first load
  useEffect(() => {
    const id = Math.random().toString(36).substring(2, 15);
    setUserId(id);
  }, []);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { text: input, sender: "user" }];
    setMessages(newMessages);
    setInput("");

    try {
      const res = await axios.post("http://localhost:5000/api/chatbot", {
        message: input,
        userId
      });

      setMessages([...newMessages, { text: res.data.reply, sender: "bot" }]);
    } catch (err) {
      setMessages([...newMessages, { text: "Error connecting to server", sender: "bot" }]);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div style={{ maxWidth: 400, margin: "50px auto", fontFamily: "Arial" }}>
      <div style={{ border: "1px solid #ccc", padding: 10, height: 450, overflowY: "scroll", marginBottom: 10, background: "#f9f9f9" }}>
        {messages.map((m, i) => (
          <div key={i} style={{ textAlign: m.sender === "user" ? "right" : "left", margin: "5px 0" }}>
            <span style={{ display: "inline-block", padding: "8px 12px", borderRadius: 15, background: m.sender === "user" ? "#007bff" : "#e0e0e0", color: m.sender === "user" ? "#fff" : "#000" }}>
              {m.text}
            </span>
          </div>
        ))}
      </div>

      <input type="text" value={input} onChange={e => setInput(e.target.value)} onKeyPress={handleKeyPress} placeholder="Type your message..." style={{ width: "80%", padding: "10px", borderRadius: 5, border: "1px solid #ccc" }} />
      <button onClick={sendMessage} style={{ width: "18%", padding: "10px", marginLeft: "2%", borderRadius: 5, border: "none", background: "#007bff", color: "#fff", cursor: "pointer" }}>Send</button>
    </div>
  );
};

export default Chatbot;
