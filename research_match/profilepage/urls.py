from django.urls import path
from . import views

urlpatterns = [
    path('profilepage/', views.hi, name='profilepage'),
]