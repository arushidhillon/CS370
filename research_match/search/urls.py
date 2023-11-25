from django.urls import path
from .views import *

urlpatterns = [
    # URL for rendering the search page
    path('search/',search, name='search_page'),

    # URL for processing the search query and returning the results
    path('search-profiles/', search_profiles, name='search_profiles'),

    # Assuming the detail view requires an 'id' parameter
    path('profile/<int:id>/',profile_detail, name='profile_detail'),
]
