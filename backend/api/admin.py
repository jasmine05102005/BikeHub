from django.contrib import admin
from .models import (
    Brand, Bike, Showroom, TestRide, Review, Favorite, 
    Notification, UpcomingLaunch, UsedBikeListing
)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'brand', 'year', 'price', 'fuel_type', 'is_featured', 'is_trending']
    list_filter = ['brand', 'fuel_type', 'condition', 'year', 'is_featured', 'is_trending']
    search_fields = ['model_name', 'brand__name']
    list_editable = ['is_featured', 'is_trending']


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone', 'is_active']
    list_filter = ['city', 'state', 'is_active']
    search_fields = ['name', 'city', 'state']


@admin.register(TestRide)
class TestRideAdmin(admin.ModelAdmin):
    list_display = ['user', 'bike', 'showroom', 'preferred_date', 'status']
    list_filter = ['status', 'preferred_date', 'created_at']
    search_fields = ['user__username', 'bike__model_name', 'showroom__name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'bike', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'bike__model_name', 'title']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'bike', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'bike__model_name']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'title', 'is_read', 'created_at']
    list_filter = ['type', 'is_read', 'created_at']
    search_fields = ['user__username', 'title']


@admin.register(UpcomingLaunch)
class UpcomingLaunchAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'brand', 'expected_launch_date', 'is_featured']
    list_filter = ['brand', 'expected_launch_date', 'is_featured']
    search_fields = ['model_name', 'brand__name']


@admin.register(UsedBikeListing)
class UsedBikeListingAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'brand', 'year', 'price', 'user', 'is_approved', 'created_at']
    list_filter = ['brand', 'year', 'condition', 'is_approved', 'created_at']
    search_fields = ['model_name', 'brand', 'user__username']
    list_editable = ['is_approved']
