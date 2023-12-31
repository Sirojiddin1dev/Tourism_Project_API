from rest_framework import serializers
from .models import User, Image, LocationCategory, LocationSubCategory, Service, Hotel, Room, \
    RoomReservation, OrderFoodToRoom, CleaningRoom, CarForRent, CarRental, Restaurant, MealCategory, \
    Meal, Table, Comment, TableReservation, Delivery, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class LocationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCategory
        fields = '__all__'


class LocationSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationSubCategory
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'


class CleaningRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningRoom
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    cleaning = CleaningRoomSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = '__all__'


class OrderFoodToRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFoodToRoom
        fields = '__all__'


class CarForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarForRent
        fields = '__all__'


class CarRentalSerializer(serializers.ModelSerializer):
    car = CarForRentSerializer()

    class Meta:
        model = CarRental
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True, read_only=True)
    img = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    category = MealCategorySerializer()

    class Meta:
        model = Meal
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TableReservationSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = TableReservation
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
