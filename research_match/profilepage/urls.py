from django.urls import path, include
from . import views
urlpatterns = [
    path('profilepage/', views.hi, name='profilepage'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('settings/', views.settings, name='settings'),
    path('matches/', views.matches, name='matches'),
]