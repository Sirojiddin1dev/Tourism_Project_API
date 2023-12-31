from django.urls import path
from .views import *

urlpatterns = [
    path('get-user/', GetUser.as_view()),
    path('update-user/', UpdateUser.as_view()),
    path('delete-user/', DeleteUser.as_view()),

    path('login/', signin_view),
    path('signup/', signup_view),
    path('logout/', logout_view),
]
