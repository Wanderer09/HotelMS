from django.urls import path
from . import views as r
from accounts import views as a
from home import views as h
urlpatterns = [
    path('',r.reception_home,name='reception_home'),
    path('guest_list/',r.guest_list,name='guest_list'),
    path('maintenance/',r.maintenance,name='maintenance'),
    path('customer/',r.customer,name='customer'),
    path('bookroom/',r.bookroom,name='bookroom'),
    path('enquiry/',r.enquiry,name='enquiry'),
    path('room_status/',r.room_status,name='room_status'),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"), 
 ]