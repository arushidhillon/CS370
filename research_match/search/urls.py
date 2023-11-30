from django.urls import path
from .views import *

urlpatterns = [
    path('opportunities/', opportunities, name='opportunities'),
    path('students/', students, name='students'),
    path('search_students/',search_students, name='search_students'),

]
