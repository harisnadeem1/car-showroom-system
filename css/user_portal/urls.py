from django.urls import path
from .views.home import index, vehicle, subscribe, car, buy, contact, about

urlpatterns = [
    path('', index),
    path('vehicle/', vehicle),
    path("sub/", subscribe),
    path("car/", car),
    path("buy/", buy),
    path("contact/", contact),
    path("about/", about)
]
