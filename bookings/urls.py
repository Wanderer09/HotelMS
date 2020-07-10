from django.urls import path,include
from . import views as b
from accounts import views as a
from home import views as h
urlpatterns = [
    path('',b.bookings,name='bookings'),
    path('booking2/',b.booking2,name="bookings2"),
    path('contact/',h.contact,name="contact_us"),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"),
   
 ]