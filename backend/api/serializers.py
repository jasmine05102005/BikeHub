from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import (
    Brand, Bike, Showroom, TestRide, Review, Favorite, 
    Notification, UpcomingLaunch, UsedBikeListing
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BikeSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    average_rating = serializers.ReadOnlyField()
    total_reviews = serializers.ReadOnlyField()

    class Meta:
        model = Bike
        fields = '__all__'


class BikeListSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    average_rating = serializers.ReadOnlyField()
    total_reviews = serializers.ReadOnlyField()

    class Meta:
        model = Bike
        fields = [
            'id', 'brand', 'brand_name', 'model_name', 'year', 'price', 
            'fuel_type', 'engine_capacity', 'mileage', 'condition',
            'main_image', 'is_featured', 'is_trending', 'average_rating', 
            'total_reviews', 'created_at'
        ]


class ShowroomSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)
    brand_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True, 
        required=False
    )

    class Meta:
        model = Showroom
        fields = '__all__'

    def create(self, validated_data):
        brand_ids = validated_data.pop('brand_ids', [])
        showroom = Showroom.objects.create(**validated_data)
        if brand_ids:
            showroom.brands.set(brand_ids)
        return showroom

    def update(self, instance, validated_data):
        brand_ids = validated_data.pop('brand_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if brand_ids is not None:
            instance.brands.set(brand_ids)
        return instance


class TestRideSerializer(serializers.ModelSerializer):
    bike_name = serializers.CharField(source='bike.model_name', read_only=True)
    bike_brand = serializers.CharField(source='bike.brand.name', read_only=True)
    showroom_name = serializers.CharField(source='showroom.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = TestRide
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    bike_name = serializers.CharField(source='bike.model_name', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class FavoriteSerializer(serializers.ModelSerializer):
    bike = BikeListSerializer(read_only=True)
    bike_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'bike', 'bike_id', 'created_at']
        read_only_fields = ['user', 'created_at']


class NotificationSerializer(serializers.ModelSerializer):
    bike_name = serializers.CharField(source='related_bike.model_name', read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['user', 'created_at']


class UpcomingLaunchSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = UpcomingLaunch
        fields = '__all__'


class UsedBikeListingSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UsedBikeListing
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


class EMICalculatorSerializer(serializers.Serializer):
    principal_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    down_payment = serializers.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    tenure_months = serializers.IntegerField()

    def validate(self, attrs):
        if attrs['down_payment'] >= attrs['principal_amount']:
            raise serializers.ValidationError("Down payment must be less than principal amount")
        return attrs


class FuelCostCalculatorSerializer(serializers.Serializer):
    monthly_km = serializers.DecimalField(max_digits=8, decimal_places=2)
    fuel_price_per_liter = serializers.DecimalField(max_digits=6, decimal_places=2)
    bike_mileage = serializers.DecimalField(max_digits=5, decimal_places=2)
