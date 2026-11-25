from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


def get_top_places(request):
    data=[
            {
             'name':'Sharm Elshiekh',
             'rating':4.5,  
            'link':'https://www.ahstatic.com/photos/b999_ho_02_p_2048x1536.jpg?utm_source=chatgpt.com',
            'Interest':['beaches']
            },
            {
                'name':'Cairo',
                'rating':4.9,
                'link':'https://images.unsplash.com/photo-1572252009286-268acec5ca0a?utm_source=chatgpt.com',
                'Interest':['Historic']
            }
    ]
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def get_options():
    transportations=TransportationSerializer(Transportation.objects.all())
    budgets=BudgetSerializer(Budget.objects.all())
    tripTypes=TripTypeSerializer(TripType.objects.all())
    interests=InterestSerializer(Interest.objects.all())
    data={
        'transportations':transportations.data,
        'budgets':budgets.data,
        'tripTypes':tripTypes.data,
        'interests':interests.data
    }
    return Response(data,many=True,statu=200)

@api_view(['GET'])
def get_place(request, place_id):
    place = Place.objects.get(id=place_id)
    serializer = PlaceSerializer(place)
    return Response(serializer.data, status=200)
