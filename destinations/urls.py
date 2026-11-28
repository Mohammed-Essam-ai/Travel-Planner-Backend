from django.urls import path
from .views import *

urlpatterns=[
    path("", home, name="home"),
    path('places/top',get_top_places), # GET
    path('places/<int:place_id>',get_place), # GET
    path('options/',get_options), # GET
    path('favourites/', favourite_places, name='favourite-places'), # GET
    path('favourites/<int:place_id>/', favourite_places, name='favourite-place'), # POST, DELETE
]
