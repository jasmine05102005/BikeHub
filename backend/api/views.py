from rest_framework import generics, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Avg, Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from decimal import Decimal
import math

from .models import (
    Brand, Bike, Showroom, TestRide, Review, Favorite, 
    Notification, UpcomingLaunch, UsedBikeListing
)
from .serializers import (
    UserSerializer, UserRegistrationSerializer, BrandSerializer, 
    BikeSerializer, BikeListSerializer, ShowroomSerializer, 
    TestRideSerializer, ReviewSerializer, FavoriteSerializer,
    NotificationSerializer, UpcomingLaunchSerializer, 
    UsedBikeListingSerializer, EMICalculatorSerializer,
    FuelCostCalculatorSerializer
)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BikeListView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'fuel_type', 'condition', 'year', 'is_featured', 'is_trending']
    search_fields = ['model_name', 'brand__name', 'description']
    ordering_fields = ['price', 'created_at', 'year', 'mileage']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Price range filter
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
            
        # Engine capacity range filter
        min_cc = self.request.query_params.get('min_cc')
        max_cc = self.request.query_params.get('max_cc')
        
        if min_cc:
            queryset = queryset.filter(engine_capacity__gte=min_cc)
        if max_cc:
            queryset = queryset.filter(engine_capacity__lte=max_cc)
            
        return queryset


class BikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SimilarBikesView(generics.ListAPIView):
    serializer_class = BikeListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        bike_id = self.kwargs['bike_id']
        try:
            bike = Bike.objects.get(id=bike_id)
            return Bike.objects.filter(
                Q(brand=bike.brand) | Q(fuel_type=bike.fuel_type) | Q(price__range=[bike.price * 0.8, bike.price * 1.2])
            ).exclude(id=bike_id)[:6]
        except Bike.DoesNotExist:
            return Bike.objects.none()


class ShowroomListView(generics.ListCreateAPIView):
    queryset = Showroom.objects.filter(is_active=True)
    serializer_class = ShowroomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city', 'state', 'brands']
    search_fields = ['name', 'city', 'state']


class ShowroomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TestRideListView(generics.ListCreateAPIView):
    serializer_class = TestRideSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return TestRide.objects.all()
        return TestRide.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TestRideDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestRideSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return TestRide.objects.all()
        return TestRide.objects.filter(user=self.request.user)


class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        bike_id = self.kwargs.get('bike_id')
        if bike_id:
            return Review.objects.filter(bike_id=bike_id)
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Review.objects.all()
        return Review.objects.filter(user=self.request.user)


class FavoriteListView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        bike_id = serializer.validated_data['bike_id']
        bike = Bike.objects.get(id=bike_id)
        favorite, created = Favorite.objects.get_or_create(
            user=self.request.user,
            bike=bike
        )
        if not created:
            favorite.delete()
            return Response({'message': 'Removed from favorites'}, status=status.HTTP_200_OK)
        return Response({'message': 'Added to favorites'}, status=status.HTTP_201_CREATED)


class FavoriteDetailView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class NotificationDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class UpcomingLaunchListView(generics.ListCreateAPIView):
    queryset = UpcomingLaunch.objects.all()
    serializer_class = UpcomingLaunchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'is_featured']


class UsedBikeListingListView(generics.ListCreateAPIView):
    queryset = UsedBikeListing.objects.filter(is_approved=True)
    serializer_class = UsedBikeListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand', 'year', 'condition', 'city', 'state']
    search_fields = ['model_name', 'brand', 'city', 'state']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UsedBikeListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsedBikeListingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return UsedBikeListing.objects.all()
        return UsedBikeListing.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def calculate_emi(request):
    serializer = EMICalculatorSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        principal = data['principal_amount'] - data['down_payment']
        rate = data['interest_rate'] / 100 / 12  # Monthly interest rate
        tenure = data['tenure_months']
        
        if rate == 0:
            emi = principal / tenure
        else:
            emi = principal * rate * (1 + rate) ** tenure / ((1 + rate) ** tenure - 1)
        
        total_amount = emi * tenure
        total_interest = total_amount - principal
        
        return Response({
            'emi': round(emi, 2),
            'total_amount': round(total_amount, 2),
            'total_interest': round(total_interest, 2),
            'principal': principal
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def calculate_fuel_cost(request):
    serializer = FuelCostCalculatorSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        monthly_km = data['monthly_km']
        fuel_price = data['fuel_price_per_liter']
        mileage = data['bike_mileage']
        
        monthly_fuel_needed = monthly_km / mileage
        monthly_cost = monthly_fuel_needed * fuel_price
        yearly_cost = monthly_cost * 12
        
        return Response({
            'monthly_fuel_needed': round(monthly_fuel_needed, 2),
            'monthly_cost': round(monthly_cost, 2),
            'yearly_cost': round(yearly_cost, 2)
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def compare_bikes(request):
    bike_ids = request.query_params.getlist('bike_ids')
    if len(bike_ids) < 2 or len(bike_ids) > 3:
        return Response({'error': 'Please select 2-3 bikes to compare'}, status=status.HTTP_400_BAD_REQUEST)
    
    bikes = Bike.objects.filter(id__in=bike_ids)
    if len(bikes) != len(bike_ids):
        return Response({'error': 'One or more bikes not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def search_suggestions(request):
    query = request.query_params.get('q', '')
    if len(query) < 2:
        return Response([])
    
    bikes = Bike.objects.filter(
        Q(model_name__icontains=query) | Q(brand__name__icontains=query)
    )[:10]
    
    suggestions = []
    for bike in bikes:
        suggestions.append({
            'id': bike.id,
            'name': f"{bike.brand.name} {bike.model_name}",
            'price': str(bike.price),
            'image': bike.main_image.url if bike.main_image else None
        })
    
    return Response(suggestions)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def dashboard_stats(request):
    total_bikes = Bike.objects.count()
    total_showrooms = Showroom.objects.filter(is_active=True).count()
    total_reviews = Review.objects.count()
    featured_bikes = Bike.objects.filter(is_featured=True)[:6]
    trending_bikes = Bike.objects.filter(is_trending=True)[:6]
    upcoming_launches = UpcomingLaunch.objects.filter(is_featured=True)[:6]
    
    return Response({
        'total_bikes': total_bikes,
        'total_showrooms': total_showrooms,
        'total_reviews': total_reviews,
        'featured_bikes': BikeListSerializer(featured_bikes, many=True).data,
        'trending_bikes': BikeListSerializer(trending_bikes, many=True).data,
        'upcoming_launches': UpcomingLaunchSerializer(upcoming_launches, many=True).data
    })
