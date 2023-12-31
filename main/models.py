from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/')
    bio = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        verbose_name='Telefon raqam',
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex='^[\+]9{2}8{1}[0-9]{9}$',
                message='Invalid phone number',
                code='invalid_number'
            ),
        ]
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Image(models.Model):
    img = models.ImageField(upload_to='img_hotel/')


class LocationCategory(models.Model):
    name = models.CharField(max_length=150)


class LocationSubCategory(models.Model):
    location_category = models.ForeignKey(LocationCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)


class Service(models.Model):
    image = models.ImageField(upload_to='service/')
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)


class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location_sub_category = models.ForeignKey(LocationSubCategory, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    call_number = models.CharField(max_length=20)
    number_rooms = models.IntegerField()
    services = models.ManyToManyField(Service, blank=True)
    car_rental = models.BooleanField(default=False)
    room_reservation = models.BooleanField(default=False)
    restaurant_and_cafe = models.BooleanField(default=False)
    restaurant_code = models.CharField(max_length=255, null=True, blank=True)
    order_food_to_room = models.BooleanField(default=False)
    shopping_mall = models.BooleanField(default=False)
    cleaning_room_service = models.BooleanField(default=False)
    rating = models.FloatField()
    images = models.ManyToManyField(Image)
    code = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_type = models.IntegerField(default=1, choices=(
        (1, 'econom'),
        (2, 'lux'),
    ))
    rooms_number = models.IntegerField()
    kitchen = models.BooleanField(default=True)
    bathroom = models.BooleanField(default=True)
    human_capacity = models.IntegerField()
    servic = models.ManyToManyField(Service)
    images = models.ManyToManyField(Image)
    cleaning = models.ForeignKey('CleaningRoom', on_delete=models.CASCADE)
    price_for_day = models.IntegerField()
    date = models.DateTimeField(auto_now=True)


class RoomReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class CleaningRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class CarForRent(models.Model):
    car_name = models.CharField(max_length=255)
    car_brand = models.CharField(max_length=255)
    car_number = models.CharField(max_length=10)
    FUEL_CHOICES = [
        ('electric', 'Electric'),
        ('gas', 'Gas'),
        ('benzine', 'Benzine'),
        ('gas_benzine', 'Gas and Benzine'),
    ]
    car_fuel = models.CharField(max_length=20, choices=FUEL_CHOICES)
    price_for_day = models.IntegerField()

    def __str__(self):
        return self.car_name


class CarRental(models.Model):
    car = models.ForeignKey(CarForRent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.car.car_name} - {self.user.username} Rental"


class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location_sub_category = models.ForeignKey(LocationSubCategory, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    number_place = models.IntegerField()
    service = models.ManyToManyField(Service, blank=True)
    delivery_service = models.BooleanField(default=False)
    call_number = models.CharField(max_length=20)
    img = models.ManyToManyField(Image)
    rating = models.FloatField()
    code = models.CharField(max_length=255, null=True, blank=True)


class MealCategory(models.Model):
    name = models.CharField(max_length=255)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()


class Table(models.Model):
    number = models.IntegerField()
    code = models.CharField(max_length=255)


class OrderFoodToRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
    time = models.DateTimeField()


class Comment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class TableReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    is_payment = models.BooleanField()


class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
    location = models.CharField(max_length=255)
    is_payment = models.BooleanField()


class Payment(models.Model):
    info = models.CharField(max_length=255)
    summa = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.summa}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.info
