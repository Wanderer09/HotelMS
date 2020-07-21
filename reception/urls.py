from django.urls import path
from . import views as r
from accounts import views as a
from home import views as h
urlpatterns = [
    path('',r.reception_home,name='reception_home'),
    path('guest_list/',r.guest_list,name='guest_list'),
    path('logout/',a.logout,name="logout"),
    path('login/',a.login,name="login"), 
 ]