from django.urls import path,include
from . import views as b
from accounts import views as a
from home import views as h
urlpatterns = [
    path('',b.bookings,name='booking'),
    path('booking2/',b.booking2,name="booking2"),
    path('booking3/',b.booking3,name="booking3"),
    path('booking4/',b.booking4,name="booking4"),
    path('handlerequest/',b.handlerequest,name="handlerequest"),
    path('contact/',h.contact,name="contact_us"),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"),
   
 ]