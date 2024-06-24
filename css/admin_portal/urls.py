from django.urls import path
from .views.home import index, login, logout, car, editcar, addcar
from .views.users import user, adduser

urlpatterns = [
    path('', index),
    path('login/', login),
    path("logout/", logout),
    path("car/", car),
    path('users/', user),
    path("editcar/", editcar),
    path('addcar/', addcar),
    path('adduser/', adduser)
]
