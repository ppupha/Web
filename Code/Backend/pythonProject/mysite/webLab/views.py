from django.shortcuts import render
from django.http import  HttpResponse

from rest_framework import viewsets

from .serializers import PlaceSerializer, CitySerializer, ReviewSerializer, ProfileSerializer, UserSerializer

from product.models import Place, City, Profile, Review
from django.contrib.auth.models import User

# Create your views here.


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('id')
    serializer_class = PlaceSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('id')
    serializer_class = CitySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer