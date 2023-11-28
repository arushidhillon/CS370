from django.urls import path
from .views import *

urlpatterns = [
    path('search',all_students, name='all_students'),
    
    path('search-students/',search_students, name='search_students'),

]
