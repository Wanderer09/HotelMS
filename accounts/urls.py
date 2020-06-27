from django.urls import path,include
from accounts import views as v
from home import views as u
from django.conf.urls import url
urlpatterns = [
    path('signup/',v.SignUp,name="signup"),
    path('login/',v.Login,name="login"),
    path('logout/',v.Logout,name="logout"),
    path('home',u.index,name='home'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate, name='activate'),
 ]
