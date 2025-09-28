@echo off
echo 🚀 Setting up Two-Wheeler Marketplace (Manual Setup)
echo.

echo 📦 Installing Python dependencies...
cd backend
pip install -r requirements.txt

echo.
echo 🔧 Setting up database...
python manage.py migrate

echo.
echo 👤 Creating admin user...
python manage.py create_superuser

echo.
echo 👤 Creating test user...
python manage.py create_test_user

echo.
echo 📊 Loading sample data...
python manage.py loaddata sample_data.json

echo.
echo ✅ Backend setup complete!
echo.
echo 🌐 Starting backend server...
echo Backend will run at: http://localhost:8000
echo Admin panel: http://localhost:8000/admin
echo.
echo 🔑 Default Credentials:
echo    Admin: admin / admin123
echo    Test User: user@example.com / password123
echo.
echo ⚠️  Keep this window open and open a new terminal for frontend setup
echo.
python manage.py runserver
