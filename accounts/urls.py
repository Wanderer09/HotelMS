from django.urls import path,include 
from accounts import views as v
from home import views as u
urlpatterns = [
    path('login/',v.login,name="login"),
    path('signup/',v.signup,name="signup"),
    path('home',u.index,name='home')
 ]
