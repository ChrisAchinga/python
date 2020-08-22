from django.urls import path
from .views import UserRegester

urlpatterns = [
    path('register/', UserRegester.as_view(), name='register')
]
