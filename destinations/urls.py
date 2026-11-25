from django.urls import path
from .views import *

urlpatterns=[
    path('places/top',get_top_places), # GET
    path('places/<int:place_id>',get_place), # GET
    path('options/',get_options), # GET
]
