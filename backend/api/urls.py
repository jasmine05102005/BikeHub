from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    # Authentication
    path('auth/register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('auth/login/', views.UserLoginView.as_view(), name='user-login'),
    path('auth/profile/', views.UserProfileView.as_view(), name='user-profile'),
    
    # Brands
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    
    # Bikes
    path('bikes/', views.BikeListView.as_view(), name='bike-list'),
    path('bikes/<int:pk>/', views.BikeDetailView.as_view(), name='bike-detail'),
    path('bikes/<int:bike_id>/similar/', views.SimilarBikesView.as_view(), name='similar-bikes'),
    
    # Showrooms
    path('showrooms/', views.ShowroomListView.as_view(), name='showroom-list'),
    path('showrooms/<int:pk>/', views.ShowroomDetailView.as_view(), name='showroom-detail'),
    
    # Test Rides
    path('test-rides/', views.TestRideListView.as_view(), name='test-ride-list'),
    path('test-rides/<int:pk>/', views.TestRideDetailView.as_view(), name='test-ride-detail'),
    
    # Reviews
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/bike/<int:bike_id>/', views.ReviewListView.as_view(), name='bike-reviews'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    
    # Favorites
    path('favorites/', views.FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(), name='favorite-detail'),
    
    # Notifications
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', views.NotificationDetailView.as_view(), name='notification-detail'),
    
    # Upcoming Launches
    path('upcoming-launches/', views.UpcomingLaunchListView.as_view(), name='upcoming-launch-list'),
    
    # Used Bike Listings
    path('used-bikes/', views.UsedBikeListingListView.as_view(), name='used-bike-list'),
    path('used-bikes/<int:pk>/', views.UsedBikeListingDetailView.as_view(), name='used-bike-detail'),
    
    # Calculators
    path('calculators/emi/', views.calculate_emi, name='emi-calculator'),
    path('calculators/fuel-cost/', views.calculate_fuel_cost, name='fuel-cost-calculator'),
    
    # Utility endpoints
    path('compare/', views.compare_bikes, name='compare-bikes'),
    path('search/suggestions/', views.search_suggestions, name='search-suggestions'),
    path('dashboard/stats/', views.dashboard_stats, name='dashboard-stats'),
]
