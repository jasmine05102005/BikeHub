# 🏍️ Two-Wheeler Marketplace

A fully functional two-wheeler marketplace web application built with React.js frontend, Django REST Framework backend, and PostgreSQL database. This is a complete, production-ready application with all features working out of the box.

## ✨ Features

### 🏠 Homepage & Dashboard
- Featured bikes carousel with trending EVs
- Search bar with auto-complete suggestions
- Quick action cards for calculators and showrooms
- Statistics overview with total bikes, showrooms, and reviews

### 🚲 Bike Listings
- Advanced filtering by brand, price, fuel type, mileage, engine capacity
- Sorting by price, popularity, newest, and more
- Grid and list view modes
- Responsive design for all screen sizes
- Real-time search with suggestions

### 🔍 Bike Details
- High-quality image carousel with navigation
- Detailed specifications and features
- User reviews and ratings system
- Similar bike recommendations
- One-click test ride booking
- Add to favorites functionality

### 🧮 Calculators
- **EMI Calculator**: Calculate monthly EMI with down payment, interest rate, and tenure
- **Fuel Cost Calculator**: Estimate monthly and yearly fuel costs
- Real-time calculations with detailed breakdowns
- Tips and recommendations for better financial planning

### 🏪 Showrooms
- Interactive map showing nearby showrooms
- Filter by city, state, and brand
- Contact information and directions
- One-click test ride booking from showroom pages

### 💰 Sell Used Bike
- Multi-step form with validation
- Image upload with preview
- Condition assessment and pricing
- Contact information and location details
- Admin approval system for listings

### 👤 User Authentication & Profiles
- Secure registration and login system
- JWT token-based authentication
- User profile management
- Favorites, test rides, and reviews tracking
- Used bike listing management

### ⭐ Reviews & Ratings
- 5-star rating system
- Verified purchase badges
- Helpful votes and comments
- Admin moderation tools

### 🔧 Admin Dashboard
- Complete bike and showroom management
- Test ride booking approval system
- Used bike listing moderation
- User management and analytics
- Real-time statistics and insights

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed
- Git installed

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd two-wheeler-marketplace
   ```

2. **Start the application**
   
   **For Windows:**
   ```bash
   # Terminal 1 - Backend
   .\setup_manual.bat
   
   # Terminal 2 - Frontend
   .\setup_frontend.bat
   ```
   
   **For Linux/Mac:**
   ```bash
   # Terminal 1 - Backend
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py create_superuser
   python manage.py create_test_user
   python manage.py loaddata sample_data.json
   python manage.py runserver
   
   # Terminal 2 - Frontend
   cd frontend
   npm install
   npm start
   ```

3. **Access the application**
   - 🌐 **Frontend**: http://localhost:3000
   - 🔧 **Backend API**: http://localhost:8000
   - 👨‍💼 **Admin Panel**: http://localhost:8000/admin

## 🔑 Default Credentials

- **Admin**: `admin` / `admin123`
- **Test User**: `user@example.com` / `password123`

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `GET /api/auth/profile/` - Get user profile

### Bikes
- `GET /api/bikes/` - List all bikes with filtering
- `GET /api/bikes/{id}/` - Get bike details
- `GET /api/bikes/{id}/similar/` - Get similar bikes
- `GET /api/search/suggestions/` - Search suggestions

### Showrooms
- `GET /api/showrooms/` - List all showrooms
- `GET /api/showrooms/{id}/` - Get showroom details

### Test Rides
- `GET /api/test-rides/` - List user's test rides
- `POST /api/test-rides/` - Book a test ride
- `PUT /api/test-rides/{id}/` - Update test ride status

### Reviews
- `GET /api/reviews/bike/{bike_id}/` - Get bike reviews
- `POST /api/reviews/` - Create a review
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

### Favorites
- `GET /api/favorites/` - Get user's favorites
- `POST /api/favorites/` - Add to favorites
- `DELETE /api/favorites/{id}/` - Remove from favorites

### Calculators
- `POST /api/calculators/emi/` - Calculate EMI
- `POST /api/calculators/fuel-cost/` - Calculate fuel cost

### Utilities
- `GET /api/compare/` - Compare bikes
- `GET /api/dashboard/stats/` - Get dashboard statistics

## 🛠️ Technology Stack

### Frontend
- **React.js 18** - Modern React with hooks
- **Material-UI 5** - Beautiful, responsive components
- **React Router 6** - Client-side routing
- **Axios** - HTTP client for API calls
- **Context API** - State management for auth and notifications

### Backend
- **Django 4.2** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Lightweight database (default)
- **JWT Authentication** - Secure token-based auth
- **Django CORS Headers** - Cross-origin resource sharing

### Database
- **SQLite** - Lightweight database (default)
- **PostgreSQL** - Production-ready database (optional)
- **Django ORM** - Object-relational mapping
- **Database migrations** - Version control for schema

### Deployment
- **SQLite** - Lightweight database (default)
- **PostgreSQL** - Production database (optional)
- **Cloudinary** - Image storage and optimization

## 📁 Project Structure

```
two-wheeler-marketplace/
├── backend/
│   ├── api/
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # API serializers
│   │   ├── views.py           # API views
│   │   ├── urls.py            # URL routing
│   │   └── admin.py           # Admin interface
│   ├── two_wheeler_marketplace/
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py            # Main URL configuration
│   │   └── management/        # Custom management commands
│   ├── sample_data.json       # Sample data fixture
│   ├── requirements.txt       # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/            # Page components
│   │   ├── contexts/         # React contexts
│   │   ├── services/         # API services
│   │   └── App.js            # Main app component
│   ├── package.json          # Node dependencies
├── setup_manual.bat        # Windows backend setup script
├── setup_frontend.bat      # Windows frontend setup script
└── README.md               # This file
```

## 🔧 Development

### Running in Development Mode

1. **Backend Development**
   ```bash
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

2. **Frontend Development**
   ```bash
   cd frontend
   npm install
   npm start
   ```

### Database Management

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load sample data
python manage.py loaddata sample_data.json

# Create superuser
python manage.py createsuperuser
```

### Adding New Features

1. **Backend**: Add models, serializers, views, and URLs
2. **Frontend**: Create components and pages
3. **API Integration**: Update services and contexts
4. **Testing**: Test all functionality end-to-end

## 🚀 Deployment

### Production Deployment

1. **Environment Variables**
   ```bash
   # Create .env file
   DATABASE_URL=postgresql://user:password@host:port/dbname
   SECRET_KEY=your-secret-key
   DEBUG=False
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   ```

2. **Production Database Setup**
   ```bash
   # For PostgreSQL production setup
   pip install psycopg2-binary
   # Update DATABASE_URL in settings.py
   python manage.py migrate
   python manage.py collectstatic
   ```

3. **Environment Variables**
   ```bash
   # Set production environment variables
   export DEBUG=False
   export SECRET_KEY=your-production-secret-key
   export DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

## 🧪 Testing

### Manual Testing Checklist

- [ ] User registration and login
- [ ] Bike browsing and filtering
- [ ] Bike details and image carousel
- [ ] Test ride booking
- [ ] EMI and fuel cost calculators
- [ ] Showroom search and booking
- [ ] Used bike listing creation
- [ ] Admin dashboard functionality
- [ ] Mobile responsiveness

### Automated Testing

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the backend logs in the terminal running `python manage.py runserver`
2. Check the frontend logs in the terminal running `npm start`
3. Restart both services: Stop and restart the terminals
4. Check the GitHub issues page

## 🎯 Roadmap

- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Payment integration
- [ ] Chat system for buyers and sellers
- [ ] AI-powered bike recommendations
- [ ] Multi-language support

---

**Built with ❤️ for bike enthusiasts**
