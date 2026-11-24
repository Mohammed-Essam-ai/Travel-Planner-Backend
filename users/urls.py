from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns=[
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # ---------------------------------
    path('register/', RegiseterView.as_view()),
    path('user/update/', UpdateUserrView.as_view()),
    path('profile/', ProfileView.as_view()),
]
