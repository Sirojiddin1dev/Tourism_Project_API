from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import (
    Image, LocationCategory, LocationSubCategory, Service, Hotel, Room,
    RoomReservation, OrderFoodToRoom, CleaningRoom, CarForRent, CarRental, Restaurant,
    MealCategory, Meal, Table, Comment, TableReservation, Delivery, Payment
)
from main.serializers import (
    ImageSerializer, LocationCategorySerializer, LocationSubCategorySerializer,
    ServiceSerializer, HotelSerializer, CleaningRoomSerializer,
    RoomSerializer, RoomReservationSerializer, OrderFoodToRoomSerializer, CarForRentSerializer, CarRentalSerializer,
    RestaurantSerializer, MealCategorySerializer, MealSerializer, TableSerializer,
    CommentSerializer, TableReservationSerializer, DeliverySerializer, PaymentSerializer
)


# Image CRUD views
class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageUpdateView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageDestroyView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


# LocationCategory CRUD views
class LocationCategoryListCreateView(generics.ListCreateAPIView):
    queryset = LocationCategory.objects.all()
    serializer_class = LocationCategorySerializer
    permission_classes = [IsAuthenticated]


class LocationCategoryUpdateView(generics.UpdateAPIView):
    queryset = LocationCategory.objects.all()
    serializer_class = LocationCategorySerializer
    permission_classes = [IsAuthenticated]


class LocationCategoryDestroyView(generics.DestroyAPIView):
    queryset = LocationCategory.objects.all()
    serializer_class = LocationCategorySerializer
    permission_classes = [IsAuthenticated]


# LocationSubCategory CRUD views
class LocationSubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = LocationSubCategory.objects.all()
    serializer_class = LocationSubCategorySerializer
    permission_classes = [IsAuthenticated]


class LocationSubCategoryUpdateView(generics.UpdateAPIView):
    queryset = LocationSubCategory.objects.all()
    serializer_class = LocationSubCategorySerializer
    permission_classes = [IsAuthenticated]


class LocationSubCategoryDestroyView(generics.DestroyAPIView):
    queryset = LocationSubCategory.objects.all()
    serializer_class = LocationSubCategorySerializer
    permission_classes = [IsAuthenticated]


# HotelService CRUD views
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


class ServiceDestroyView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


# Hotel CRUD views
class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


class HotelUpdateView(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


class HotelDestroyView(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


# CleaningRoom CRUD views
class CleaningRoomListCreateView(generics.ListCreateAPIView):
    queryset = CleaningRoom.objects.all()
    serializer_class = CleaningRoomSerializer
    permission_classes = [IsAuthenticated]


class CleaningRoomUpdateView(generics.UpdateAPIView):
    queryset = CleaningRoom.objects.all()
    serializer_class = CleaningRoomSerializer
    permission_classes = [IsAuthenticated]


class CleaningRoomDestroyView(generics.DestroyAPIView):
    queryset = CleaningRoom.objects.all()
    serializer_class = CleaningRoomSerializer
    permission_classes = [IsAuthenticated]


# Room CRUD views
class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomUpdateView(generics.UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomDestroyView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


# RoomReservation CRUD views
class RoomReservationListCreateView(generics.ListCreateAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    permission_classes = [IsAuthenticated]


class RoomReservationUpdateView(generics.UpdateAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    permission_classes = [IsAuthenticated]


class RoomReservationDestroyView(generics.DestroyAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    permission_classes = [IsAuthenticated]


# OrderFoodToRoom CRUD views
class OrderFoodToRoomListCreateView(generics.ListCreateAPIView):
    queryset = OrderFoodToRoom.objects.all()
    serializer_class = OrderFoodToRoomSerializer
    permission_classes = [IsAuthenticated]


class OrderFoodToRoomUpdateView(generics.UpdateAPIView):
    queryset = OrderFoodToRoom.objects.all()
    serializer_class = OrderFoodToRoomSerializer
    permission_classes = [IsAuthenticated]


class OrderFoodToRoomDestroyView(generics.DestroyAPIView):
    queryset = OrderFoodToRoom.objects.all()
    serializer_class = OrderFoodToRoomSerializer
    permission_classes = [IsAuthenticated]


# CarForRent CRUD views
class CarForRentListCreateView(generics.ListCreateAPIView):
    queryset = CarForRent.objects.all()
    serializer_class = CarForRentSerializer
    permission_classes = [IsAuthenticated]


class CarForRentUpdateView(generics.UpdateAPIView):
    queryset = CarForRent.objects.all()
    serializer_class = CarForRentSerializer
    permission_classes = [IsAuthenticated]


class CarForRentDestroyView(generics.DestroyAPIView):
    queryset = CarForRent.objects.all()
    serializer_class = CarForRentSerializer
    permission_classes = [IsAuthenticated]


# CarRental CRUD views
class CarRentalListCreateView(generics.ListCreateAPIView):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer
    permission_classes = [IsAuthenticated]


class CarRentalUpdateView(generics.UpdateAPIView):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer
    permission_classes = [IsAuthenticated]


class CarRentalDestroyView(generics.DestroyAPIView):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer
    permission_classes = [IsAuthenticated]


# Restaurant CRUD views
class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class RestaurantDestroyView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


# MealCategory CRUD views
class MealCategoryListCreateView(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer
    permission_classes = [IsAuthenticated]


class MealCategoryUpdateView(generics.UpdateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer
    permission_classes = [IsAuthenticated]


class MealCategoryDestroyView(generics.DestroyAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer
    permission_classes = [IsAuthenticated]


# Meal CRUD views
class MealListCreateView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]


class MealUpdateView(generics.UpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]


class MealDestroyView(generics.DestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]


# Table CRUD views
class TableListCreateView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


class TableUpdateView(generics.UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


class TableDestroyView(generics.DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


# Order CRUD views
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentDestroyView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


# TableReservation CRUD views
class TableReservationListCreateView(generics.ListCreateAPIView):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer
    permission_classes = [IsAuthenticated]


class TableReservationUpdateView(generics.UpdateAPIView):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer
    permission_classes = [IsAuthenticated]


class TableReservationDestroyView(generics.DestroyAPIView):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer
    permission_classes = [IsAuthenticated]


# Delivery CRUD views
class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]


class DeliveryUpdateView(generics.UpdateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]


class DeliveryDestroyView(generics.DestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]


# Payment CRUD views
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDestroyView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
