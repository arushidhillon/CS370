from django.urls import path
from .views import *

urlpatterns = [
    path('students/',all_students, name='all_students'),
    
    path('search_students/',search_students, name='search_students'),

]
