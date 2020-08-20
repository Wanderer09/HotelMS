from django.urls import path
from . import views as m
from accounts import views as a
urlpatterns = [
    path('',m.hotel_manager,name='hotel-manager'),
    path('restaurant-manager',m.restro_manager,name='restro_manager'),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"), 
 ]