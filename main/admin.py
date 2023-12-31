from django.contrib import admin
from .models import *

# Registering User model
admin.site.register(User)

# Registering Image models
admin.site.register(Image)

# Registering LocationCategory and LocationSubCategory models
admin.site.register(LocationCategory)
admin.site.register(LocationSubCategory)

# Registering Service and Hotel models
admin.site.register(Service)
admin.site.register(Hotel)

# Registering Room, RoomReservation, OrderFoodToRoom, CleaningRoom models

admin.site.register(Room)
admin.site.register(RoomReservation)
admin.site.register(OrderFoodToRoom)
admin.site.register(CleaningRoom)

# Registering CarForRent and CarRental models
admin.site.register(CarForRent)
admin.site.register(CarRental)

# Registering Restaurant models
admin.site.register(Restaurant)

# Registering MealCategory, Meal, Table, Order, TableReservation, Delivery models
admin.site.register(MealCategory)
admin.site.register(Meal)
admin.site.register(Table)
admin.site.register(Comment)
admin.site.register(TableReservation)
admin.site.register(Delivery)

# Registering Payment model
admin.site.register(Payment)
