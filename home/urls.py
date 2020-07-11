from django.urls import path
from . import views
from home import views
from accounts import views as a
urlpatterns = [
    path('',views.index,name="Home"),
    path('contact/',views.contact,name="contact_us"),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"),
    path('booking/',views.booking,name="booking"),
    path('booking2/',views.booking2,name="booking"), 
    path('booking3/',views.booking3,name="booking"),  
]
