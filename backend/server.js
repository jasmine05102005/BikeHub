import dotenv from "dotenv";
import express from "express";
import cors from "cors";
import mongoose from "mongoose";

import serviceRoutes from "./routes/serviceRoutes.js";
import chatbotRoutes from "./routes/chatbotRoutes.js";
import bookingRoutes from "./routes/bookingRoutes.js"; 

dotenv.config();

// 1️⃣ Initialize Express app
const app = express();

// 2️⃣ Middleware
app.use(cors());
app.use(express.json());

// 3️⃣ Routes
app.use("/api/services", serviceRoutes);
app.use("/api/chatbot", chatbotRoutes);
app.use("/api/bookings", bookingRoutes);  // <-- now it's safe

// 4️⃣ Connect to MongoDB and start server
const PORT = process.env.PORT || 5000;

mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log("MongoDB connected");
    app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
  })
  .catch(err => console.error(err));
