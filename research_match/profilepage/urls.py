from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('signout', views.signout, name ="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('profilepage/', views.studenthomepage, name='profilepage'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('settings/', views.settings, name='settings'),
    path('matches/', views.matches, name='matches'),
]