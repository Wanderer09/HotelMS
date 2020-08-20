from django.urls import path,include 
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from reception import views as r
from traveldesk import views as t
from accounts import views as v
from home import views as u
urlpatterns = [
    path('social/', include('allauth.urls')),
    path('signup/',v.signup,name="signup"),
    path('login/',v.login,name="login"),
    path('reception/',r.reception_home,name="reception"),
    path('travel_desk/',t.traveldesk_home,name="travel_desk"),
    path('admin-login/',v.admin,name="admin-login"),
    path('logout/',v.logout,name="logout"),
    path('home',u.index,name='home'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate_account, name='activate'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
 ]