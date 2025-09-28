#!/bin/bash

echo "🚀 Setting up Frontend (Manual Setup)"
echo

echo "📦 Installing Node.js dependencies..."
cd frontend
npm install

echo
echo "✅ Frontend setup complete!"
echo
echo "🌐 Starting frontend server..."
echo "Frontend will run at: http://localhost:3000"
echo
echo "⚠️  Make sure backend is running on http://localhost:8000"
echo
npm start
