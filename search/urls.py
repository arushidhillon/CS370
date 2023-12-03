from django.urls import path
from . import views

urlpatterns = [
    # URL for rendering the search page
    path('search/', views.search, name='search_page'),
    # URL for processing the search query and returning the results
    path('search-profiles/', views.list_profiles, name='search_profiles'),
]
