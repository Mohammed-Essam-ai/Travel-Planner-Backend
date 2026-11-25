from django.shortcuts import render
from django.http.response import JsonResponse 

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
