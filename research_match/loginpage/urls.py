from . import views
from django.contrib import admin
from django.urls import path, include

app_name = "profile"
urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('signout', views.signout, name ="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate")

]