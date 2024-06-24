from django.urls import path
from .views.home import index, login, car, editcar, addcar, orders

urlpatterns = [
    path('', index),
    path('login/', login),
    path("car/", car),
    path("editcar/", editcar),
    path('addcar/', addcar), 
    path('orders/', orders)
]
