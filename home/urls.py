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
    path('booking4/',views.booking4,name="booking"), 
    path('reception/',views.reception,name="booking"), 
    path('guestlist/',views.guestlist,name="booking"),
    path('rooms/',views.rooms,name="booking"), 
    path('maintain/',views.maintain,name="booking"), 
    path('bookroom/',views.bookroom,name="booking"),
    path('enquiry/',views.enquiry,name="booking"),
    path('customer/',views.customer,name="booking"),
    path('aboutus/',views.aboutus,name="booking"),
    path('manager/',views.manager,name="booking"),
    path('travel/',views.travel,name="booking"),
    path('pick/',views.pick,name="booking"),
    path('rent/',views.rental,name="booking"),
    path('driver/',views.driver,name="booking"),
    path('car/',views.car,name="booking"),
    path('admin-login/',views.admin,name="booking"),
    path('hotel-manager/',views.hotel,name="booking"),
    path('add-employee/',views.add,name="booking"),

]

