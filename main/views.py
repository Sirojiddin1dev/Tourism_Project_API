from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# ---------------------  FILTER FUNCTIONS -----------------


# Location Filters
@api_view(['GET'])
def location_category_by_location(request, location_category_id):
    location_category = get_object_or_404(LocationCategory, id=location_category_id)
    sub_categories = LocationSubCategory.objects.filter(category=location_category)
    serializer = LocationSubCategorySerializer(sub_categories, many=True)
    return Response(serializer.data)


# Hotel Filters
@api_view(['GET'])
def hotels_by_sub_category(request, sub_category_id):
    hotels = Hotel.objects.filter(sub_category=sub_category_id)
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hotels_by_service(request, service_id):
    hotels = Hotel.objects.filter(services=service_id)
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hotels_by_room_type(request, room_type_id):
    hotels = Hotel.objects.filter(rooms__room_type=room_type_id)
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


# Restaurant Filters
@api_view(['GET'])
def restaurants_by_sub_category(request, sub_category_id):
    restaurants = Restaurant.objects.filter(sub_category=sub_category_id)
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def restaurants_by_service(request, service_id):
    restaurants = Restaurant.objects.filter(services=service_id)
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def restaurants_by_table_capacity(request, capacity):
    restaurants = Restaurant.objects.filter(tables__capacity__gte=capacity)
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


# Room Filters
@api_view(['GET'])
def rooms_by_hotel(request, hotel_id):
    rooms = Room.objects.filter(hotel=hotel_id)
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def room_reservations_by_hotel(request, hotel_id):
    reservations = RoomReservation.objects.filter(room__hotel=hotel_id)
    serializer = RoomReservationSerializer(reservations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def order_food_to_rooms_by_hotel(request, hotel_id):
    orders = OrderFoodToRoom.objects.filter(room__hotel=hotel_id)
    serializer = OrderFoodToRoomSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def car_for_rents_by_hotel(request, hotel_id):
    cars = CarForRent.objects.filter(hotel=hotel_id)
    serializer = CarForRentSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def car_rentals_by_hotel(request, hotel_id):
    rentals = CarRental.objects.filter(hotel=hotel_id)
    serializer = CarRentalSerializer(rentals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def cleaning_rooms_by_hotel(request, hotel_id):
    cleaning_rooms = CleaningRoom.objects.filter(hotel=hotel_id)
    serializer = CleaningRoomSerializer(cleaning_rooms, many=True)
    return Response(serializer.data)


# Restaurant by Code
@api_view(['GET'])
def restaurant_by_code(request, restaurant_code):
    restaurant = get_object_or_404(Restaurant, code=restaurant_code)
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)


# Table by Restaurant
@api_view(['GET'])
def tables_by_restaurant(request, restaurant_id):
    tables = Table.objects.filter(restaurant=restaurant_id)
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)


# Table Reservation by Restaurant
@api_view(['GET'])
def table_reservations_by_restaurant(request, restaurant_id):
    reservations = TableReservation.objects.filter(table__restaurant=restaurant_id)
    serializer = TableReservationSerializer(reservations, many=True)
    return Response(serializer.data)


# Delivery by Restaurant
@api_view(['GET'])
def deliveries_by_restaurant(request, restaurant_id):
    deliveries = Delivery.objects.filter(restaurant=restaurant_id)
    serializer = DeliverySerializer(deliveries, many=True)
    return Response(serializer.data)


# Table by Human Capacity
@api_view(['GET'])
def tables_by_human_capacity(request, capacity):
    tables = Table.objects.filter(capacity=capacity)
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)
