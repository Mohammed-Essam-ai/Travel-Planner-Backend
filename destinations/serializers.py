from rest_framework import serializers
from .models import *


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields='__all__'


class FavouritePlaceSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = FavouritePlace
        fields = ("id", "place", "created_at")


class TripTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TripType
        fields='__all__'


class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transportation
        fields='__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interest
        fields='__all__'        


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Budget
        fields='__all__'
