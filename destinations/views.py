from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FavouritePlace
from .serializers import FavouritePlaceSerializer


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

def home(request):
    return HttpResponse("Travel Planner API is running successfully!")
    
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


@api_view(['GET', 'POST', 'DELETE'])
def favourite_places(request, place_id=None):
    if not request.user.is_authenticated:
        return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        favourites = FavouritePlace.objects.filter(user=request.user).select_related('place')
        return Response(FavouritePlaceSerializer(favourites, many=True).data, status=status.HTTP_200_OK)

    place = get_object_or_404(Place, id=place_id)
    if request.method == 'POST':
        favourite, created = FavouritePlace.objects.get_or_create(user=request.user, place=place)
        return Response(
            FavouritePlaceSerializer(favourite).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    deleted, _ = FavouritePlace.objects.filter(user=request.user, place=place).delete()
    if not deleted:
        return Response({'detail': 'Place is not in favourites.'}, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_204_NO_CONTENT)
