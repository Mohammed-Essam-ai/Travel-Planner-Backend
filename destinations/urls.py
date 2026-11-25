from django.urls import path
from .views import *

urlpatterns=[
    path('places/top',get_top_places)
]