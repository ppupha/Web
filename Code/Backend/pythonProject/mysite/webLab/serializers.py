from django.db import models
from django.db.models import fields
from rest_framework import serializers

from product.models import Place, City, Review, Profile
import django.contrib.auth.models as md


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    #City = serializers.HyperlinkedRelatedField(many=True, view_name='city-detail', read_only=True)
    class Meta:
        model = Place
        fields = ('Name', 'Rating', 'Address',
                  'Description', 'Type', 'Site', 'Tel',)

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('Name',)

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'user',)

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('comment', 'createTime', 'rating',)


