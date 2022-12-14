from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class DirectorListSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'name movies movies_count'.split()

    def get_movies(self, obj_director):
        return [director.title for director in obj_director.movies.all()]

    def get_movies_count(self, obj_director):
        return obj_director.movies.count()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'text'.split()


class MovieReviewListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()

    def get_reviews(self, obj_movie):
        return [rev.text for rev in obj_movie.reviews.all()]

    def get_rating(self, obj_movie):
        summ = 0
        for s in obj_movie.reviews.all():
            summ += s.stars
        return round(summ / obj_movie.reviews.count(), 1) if obj_movie.reviews.count() else 'No Rating'



class MoviesBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(default='30')
    director = serializers.IntegerField(min_value=1)

    def validate_director(self, id):
        try:
            Director.objects.get(id=id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id={id} Not Found')
        return id

class ReviewBaseValidateSerializer(serializers.Serializer):

    text = serializers.CharField()




class MoviesCreateSerializer(MoviesBaseValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError('Title must be unic')
        return title