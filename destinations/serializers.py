from rest_framework import serializers
from .models import *


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields='__all__'


class TripTypeSerializer(model.ModelSerializer):
    class Meta:
        model=TripType
        fields='__all__'


class TransportationSerializer(model.ModelSerializer):
    class Meta:
        model=Transportation
        fields='__all__'


class InterestSerializer(model.ModelSerializer):
    class Meta:
        model=Interest
        fields='__all__'        


class BudgetSerializer(model.ModelSerializer):
    class Meta:
        model=Budget
        fields='__all__'