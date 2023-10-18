from django.urls import path
from . import views

urlpatterns = [
    path('profilepage/', views.hi, name='profilepage'),
    path('profilepage/', views.get_skill, name='profilepage')
]