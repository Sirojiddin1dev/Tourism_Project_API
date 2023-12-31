from django.urls import path
from .views import (
    ImageListCreateView, ImageUpdateView, ImageDestroyView,
    LocationCategoryListCreateView, LocationCategoryUpdateView, LocationCategoryDestroyView,
    LocationSubCategoryListCreateView, LocationSubCategoryUpdateView, LocationSubCategoryDestroyView,
    ServiceListCreateView, ServiceUpdateView, ServiceDestroyView,
    HotelListCreateView, HotelUpdateView, HotelDestroyView,
    CleaningRoomListCreateView, CleaningRoomUpdateView, CleaningRoomDestroyView,
    RoomListCreateView, RoomUpdateView, RoomDestroyView,
    RoomReservationListCreateView, RoomReservationUpdateView, RoomReservationDestroyView,
    OrderFoodToRoomListCreateView, OrderFoodToRoomUpdateView, OrderFoodToRoomDestroyView,
    CarForRentListCreateView, CarForRentUpdateView, CarForRentDestroyView,
    CarRentalListCreateView, CarRentalUpdateView, CarRentalDestroyView,
    RestaurantListCreateView, RestaurantUpdateView, RestaurantDestroyView,
    MealCategoryListCreateView, MealCategoryUpdateView, MealCategoryDestroyView,
    MealListCreateView, MealUpdateView, MealDestroyView,
    TableListCreateView, TableUpdateView, TableDestroyView,
    CommentListCreateView, CommentUpdateView, CommentDestroyView,
    TableReservationListCreateView, TableReservationUpdateView, TableReservationDestroyView,
    DeliveryListCreateView, DeliveryUpdateView, DeliveryDestroyView,
    PaymentListCreateView, PaymentUpdateView, PaymentDestroyView,
)

urlpatterns = [
    path('images/', ImageListCreateView.as_view()),
    path('images/<int:pk>/', ImageUpdateView.as_view()),
    path('images/<int:pk>/delete/', ImageDestroyView.as_view()),

    path('location-categories/', LocationCategoryListCreateView.as_view()),
    path('location-categories/<int:pk>/', LocationCategoryUpdateView.as_view()),
    path('location-categories/<int:pk>/delete/', LocationCategoryDestroyView.as_view()),

    path('location-sub-categories/', LocationSubCategoryListCreateView.as_view()),
    path('location-sub-categories/<int:pk>/', LocationSubCategoryUpdateView.as_view()),
    path('location-sub-categories/<int:pk>/delete/', LocationSubCategoryDestroyView.as_view()),

    path('services/', ServiceListCreateView.as_view()),
    path('services/<int:pk>/', ServiceUpdateView.as_view()),
    path('services/<int:pk>/delete/', ServiceDestroyView.as_view()),

    path('hotels/', HotelListCreateView.as_view()),
    path('hotels/<int:pk>/', HotelUpdateView.as_view()),
    path('hotels/<int:pk>/delete/', HotelDestroyView.as_view()),

    path('cleaning-rooms/', CleaningRoomListCreateView.as_view()),
    path('cleaning-rooms/<int:pk>/', CleaningRoomUpdateView.as_view()),
    path('cleaning-rooms/<int:pk>/delete/', CleaningRoomDestroyView.as_view()),

    path('rooms/', RoomListCreateView.as_view()),
    path('rooms/<int:pk>/', RoomUpdateView.as_view()),
    path('rooms/<int:pk>/delete/', RoomDestroyView.as_view()),

    path('room-reservations/', RoomReservationListCreateView.as_view()),
    path('room-reservations/<int:pk>/', RoomReservationUpdateView.as_view()),
    path('room-reservations/<int:pk>/delete/', RoomReservationDestroyView.as_view()),

    path('order-food-to-rooms/', OrderFoodToRoomListCreateView.as_view()),
    path('order-food-to-rooms/<int:pk>/', OrderFoodToRoomUpdateView.as_view()),
    path('order-food-to-rooms/<int:pk>/delete/', OrderFoodToRoomDestroyView.as_view()),

    # ---------------------  CarForRent CRUD -----------------
    path('car-for-rents/', CarForRentListCreateView.as_view()),
    path('car-for-rents/<int:pk>/', CarForRentUpdateView.as_view()),
    path('car-for-rents/<int:pk>/delete/', CarForRentDestroyView.as_view()),

    # ---------------------  CarRental CRUD -----------------
    path('car-rentals/', CarRentalListCreateView.as_view()),
    path('car-rentals/<int:pk>/', CarRentalUpdateView.as_view()),
    path('car-rentals/<int:pk>/delete/', CarRentalDestroyView.as_view()),

    # ---------------------  Restaurant CRUD -----------------
    path('restaurants/', RestaurantListCreateView.as_view()),
    path('restaurants/<int:pk>/', RestaurantUpdateView.as_view()),
    path('restaurants/<int:pk>/delete/', RestaurantDestroyView.as_view()),

    # ---------------------  MealCategory CRUD -----------------
    path('meal-categories/', MealCategoryListCreateView.as_view()),
    path('meal-categories/<int:pk>/', MealCategoryUpdateView.as_view()),
    path('meal-categories/<int:pk>/delete/', MealCategoryDestroyView.as_view()),

    # ---------------------  Meal CRUD -----------------
    path('meals/', MealListCreateView.as_view()),
    path('meals/<int:pk>/', MealUpdateView.as_view()),
    path('meals/<int:pk>/delete/', MealDestroyView.as_view()),

    # ---------------------  Table CRUD -----------------
    path('tables/', TableListCreateView.as_view()),
    path('tables/<int:pk>/', TableUpdateView.as_view()),
    path('tables/<int:pk>/delete/', TableDestroyView.as_view()),

    # ---------------------  Order CRUD -----------------
    path('Comment/', CommentListCreateView.as_view()),
    path('Comment/<int:pk>/', CommentUpdateView.as_view()),
    path('Comment/<int:pk>/delete/', CommentDestroyView.as_view()),

    # ---------------------  TableReservation CRUD -----------------
    path('table-reservations/', TableReservationListCreateView.as_view()),
    path('table-reservations/<int:pk>/', TableReservationUpdateView.as_view()),
    path('table-reservations/<int:pk>/delete/', TableReservationDestroyView.as_view()),

    # ---------------------  Delivery CRUD -----------------
    path('deliveries/', DeliveryListCreateView.as_view()),
    path('deliveries/<int:pk>/', DeliveryUpdateView.as_view()),
    path('deliveries/<int:pk>/delete/', DeliveryDestroyView.as_view()),

    # ---------------------  Payment CRUD -----------------
    path('payments/', PaymentListCreateView.as_view()),
    path('payments/<int:pk>/', PaymentUpdateView.as_view()),
    path('payments/<int:pk>/delete/', PaymentDestroyView.as_view()),
]
