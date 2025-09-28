import mongoose from "mongoose";
import dotenv from "dotenv";
import Service from "./models/Service.js";
import Faq from "./models/Faq.js";

dotenv.config();

mongoose.connect(process.env.MONGO_URI)
  .then(async () => {
    console.log("Connected to DB for seeding");

    await Service.deleteMany({});
    await Service.insertMany([
      { name: "Brake Check", description: "Brake pads & rotor inspection", price: 800, durationMins: 45 },
      { name: "Full Vehicle Inspection", description: "Engine, brakes, AC, electrical", price: 2500, durationMins: 90 },
      { name: "Oil Change", description: "Engine oil + filter", price: 1200, durationMins: 30 }
    ]);

    await Faq.deleteMany({});
    await Faq.insertMany([
      { question: "What is the cost of an oil change?", answer: "₹1200 for standard oil change." },
      { question: "Where is the nearest service center?", answer: "We have centers in Hyderabad, Bangalore, and Guntur." }
    ]);

    console.log("Seeded services and FAQs");
    process.exit();
  })
  .catch(err => console.error(err));
