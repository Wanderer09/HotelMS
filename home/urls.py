from django.urls import path
from . import views
from home import views
from accounts import views as a

urlpatterns = [
    path('',views.index,name="Home"),
    path('contact/',views.contact,name="contact_us"),
    path('login/',a.Login,name='login'),
    path('logout/',a.Logout,name='logout'),
]
