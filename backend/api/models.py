from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bike(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('certified_used', 'Certified Used'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='bikes')
    model_name = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    engine_capacity = models.IntegerField(help_text="Engine capacity in CC")
    mileage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Mileage in km/l")
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField()
    specifications = models.JSONField(default=dict, blank=True)
    features = models.JSONField(default=list, blank=True)
    main_image = models.ImageField(upload_to='bikes/')
    images = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    stock_quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand.name} {self.model_name} ({self.year})"

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0

    @property
    def total_reviews(self):
        return self.reviews.count()


class Showroom(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    brands = models.ManyToManyField(Brand, related_name='showrooms')
    image = models.ImageField(upload_to='showrooms/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city}"


class TestRide(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_rides')
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='test_rides')
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, related_name='test_rides')
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.bike} - {self.preferred_date}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=200)
    comment = models.TextField()
    is_verified_purchase = models.BooleanField(default=False)
    helpful_votes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'bike']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.bike} - {self.rating} stars"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'bike']

    def __str__(self):
        return f"{self.user.username} - {self.bike}"


class Notification(models.Model):
    TYPE_CHOICES = [
        ('test_ride_confirmed', 'Test Ride Confirmed'),
        ('test_ride_cancelled', 'Test Ride Cancelled'),
        ('price_drop', 'Price Drop'),
        ('new_bike', 'New Bike Available'),
        ('review_response', 'Review Response'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    related_bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class UpcomingLaunch(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='upcoming_launches')
    model_name = models.CharField(max_length=200)
    expected_price_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expected_price_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expected_launch_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='upcoming/')
    features = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['expected_launch_date']

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"


class UsedBikeListing(models.Model):
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='used_bike_listings')
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField(help_text="Total mileage in km")
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField()
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='bikes/')
    images = models.JSONField(default=list, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.year}) - {self.user.username}"
