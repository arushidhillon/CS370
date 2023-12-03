from django.urls import path
from . import views

urlpatterns = [
    # URL for rendering the search page
    path('students/', students, name='students'),
    path('search_students/',search_students, name='search_students'),
]
