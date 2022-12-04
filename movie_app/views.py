from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Director, Review, Movie
from movie_app.serializers import *
from rest_framework import status



@api_view(['GET'])
def directors_view(request):

    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def one_director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    if request.method == "GET":
        return Response(data=DirectorSerializer(director).data)

@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieListSerializer(movies, many=True).data
        return Response(data=data)



@api_view(['GET', 'PUT', 'DELETE'])
def one_movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    if request.method == 'GET':
        return Response(data=MovieListSerializer(movie).data)



@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data)




@api_view(['GET', 'PUT', 'DELETE'])
def one_review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found'})
    if request.method == 'GET':
        return Response(ReviewListSerializer(review).data)

@api_view(['GET'])
def movies_reviews_view(request):
    movies_reviews = Movie.objects.all()
    data = MovieReviewListSerializer(movies_reviews, many=True).data
    return Response(data=data)



