from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class DirectorSerializer(serializers.ModelSerializer):
     class Meta:
        model = Director
        fields = 'name '.split()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'text'.split()