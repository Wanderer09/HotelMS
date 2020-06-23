from django.urls import path
from . import views
from accounts import views

urlpatterns = [
    path('',views.login,name="login"),
]
