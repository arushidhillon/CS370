from django.urls import path
from .views import *

urlpatterns = [
    path('search_students/',search_students, name='search_students'),

]
