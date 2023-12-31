from django.urls import path
from .views import *

urlpatterns = [
    # Location Filters
    path('location-categories/<int:location_category_id>/sub-categories/', location_category_by_location),

    # Hotel Filters
    path('hotels/sub-categories/<int:sub_category_id>/', hotels_by_sub_category),
    path('hotels/services/<int:service_id>/', hotels_by_service),
    path('hotels/room-types/<int:room_type_id>/', hotels_by_room_type),

    # Restaurant Filters
    path('restaurants/sub-categories/<int:sub_category_id>/', restaurants_by_sub_category),
    path('restaurants/services/<int:service_id>/', restaurants_by_service),
    path('restaurants/table-capacity/<int:capacity>/', restaurants_by_table_capacity),

    # Room Filters
    path('rooms/hotels/<int:hotel_id>/', rooms_by_hotel),
    path('room-reservations/hotels/<int:hotel_id>/', room_reservations_by_hotel),
    path('order-food-to-rooms/hotels/<int:hotel_id>/', order_food_to_rooms_by_hotel),
    path('car-for-rents/hotels/<int:hotel_id>/', car_for_rents_by_hotel),
    path('car-rentals/hotels/<int:hotel_id>/', car_rentals_by_hotel),
    path('cleaning-rooms/hotels/<int:hotel_id>/', cleaning_rooms_by_hotel),

    # Restaurant by Code
    path('restaurants/code/<str:restaurant_code>/', restaurant_by_code),

    # Table by Restaurant
    path('tables/restaurants/<int:restaurant_id>/', tables_by_restaurant),

    # Table Reservation by Restaurant
    path('table-reservations/restaurants/<int:restaurant_id>/', table_reservations_by_restaurant),

    # Delivery by Restaurant
    path('deliveries/restaurants/<int:restaurant_id>/', deliveries_by_restaurant),

    # Table by Human Capacity
    path('tables/human-capacity/<int:capacity>/', tables_by_human_capacity),
]

