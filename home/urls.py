from django.urls import path
from . import views
from home import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('contact/',views.contact,name="contact_us"),
]
