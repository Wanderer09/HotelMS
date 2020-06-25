from django.urls import path,include 
from accounts import views as v
from home import views as u
urlpatterns = [
    path('signup/',v.SignUp,name="signup"),
    path('login/',v.Login,name="login"),
    path('logout/',v.LogoutUser,name="logout"),
    path('home',u.index,name='home')
 ]
