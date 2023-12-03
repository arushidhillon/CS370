from django.urls import path
from .views import *

urlpatterns = [
    # URL for rendering the search page
    path('students/',students, name='students'),
    # URL for processing the search query and returning the results
    path('search-students/',search_students, name='search_students'),
]
