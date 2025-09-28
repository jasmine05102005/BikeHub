# 🚀 Two-Wheeler Marketplace - Run Instructions

## ✅ **Docker Removed - Manual Setup Only**

The project has been completely cleaned of Docker dependencies and now runs with simple Python and Node.js setup.

## 🛠️ **Prerequisites**

- **Python 3.8+** installed
- **Node.js 16+** installed  
- **Git** installed

## 🚀 **Quick Start (Windows)**

### **Step 1: Setup Backend**
```powershell
.\setup_manual.bat
```

### **Step 2: Setup Frontend (New Terminal)**
```powershell
.\setup_frontend.bat
```

## 🚀 **Quick Start (Linux/Mac)**

### **Step 1: Setup Backend**
```bash
chmod +x setup_manual.sh
./setup_manual.sh
```

### **Step 2: Setup Frontend (New Terminal)**
```bash
chmod +x setup_frontend.sh
./setup_frontend.sh
```

## 🚀 **Manual Setup (Step by Step)**

### **Backend Setup:**
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py create_superuser
python manage.py create_test_user
python manage.py loaddata sample_data.json
python manage.py runserver
```

### **Frontend Setup (New Terminal):**
```bash
cd frontend
npm install
npm start
```

## 🌐 **Access URLs**

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 🔑 **Default Credentials**

- **Admin**: `admin` / `admin123`
- **Test User**: `user@example.com` / `password123`

## 📊 **What's Included**

- ✅ **SQLite Database** (no PostgreSQL setup needed)
- ✅ **Sample Data** (6 bikes, 3 showrooms, users, reviews)
- ✅ **All Features Working** (same as before)
- ✅ **No Docker Required**
- ✅ **Easy Setup** (just Python + Node.js)

## 🛠️ **Database**

- **Default**: SQLite (file-based, no setup needed)
- **Optional**: PostgreSQL (for production)

## 🔧 **Troubleshooting**

### **Backend Issues:**
```bash
# Check if Python is installed
python --version

# Check if pip is working
pip --version

# Install requirements manually
pip install -r backend/requirements.txt
```

### **Frontend Issues:**
```bash
# Check if Node.js is installed
node --version

# Check if npm is working
npm --version

# Install dependencies manually
cd frontend
npm install
```

### **Port Conflicts:**
- Backend runs on port 8000
- Frontend runs on port 3000
- Make sure these ports are free

## 🎯 **All Features Working**

- ✅ Homepage with featured bikes
- ✅ Bike listings with filters
- ✅ Bike details with image carousel
- ✅ Compare bikes functionality
- ✅ EMI and fuel cost calculators
- ✅ Showroom search and booking
- ✅ Sell used bike form
- ✅ User authentication
- ✅ Reviews and ratings
- ✅ Admin dashboard
- ✅ Mobile responsive design

## 🚀 **Ready to Run!**

Just run the setup scripts and you're good to go! The application works exactly the same as before, just without Docker complexity.
