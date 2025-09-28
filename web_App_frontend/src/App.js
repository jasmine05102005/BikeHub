import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import Navbar from "./components/common/Navbar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import Logout from "./components/auth/Logout";
import Dashboard from "./components/Dashboard";
import PrivateRoute from "./components/common/PrivateRoute";
import BikeList from "./components/BikeList";
import ShowroomList from "./components/Showroom";
import BikeCard from "./services/api";

function App() {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <div style={{ padding: "20px" }}>
          <Routes>
            <Route path="/" element={<h1>Welcome to BikeHub</h1>} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/bikes" element={<BikeList />} />
            <Route path="/showrooms" element={<ShowroomList />} />

            <Route
              path="/dashboard"
              element={
                <PrivateRoute>
                  <Dashboard />
                </PrivateRoute>
              }
            />

            <Route path="/logout" element={<Logout />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
