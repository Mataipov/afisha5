from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Director, Review, Movie
from movie_app.serializers import *
from rest_framework import status



@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorListSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MoviesBaseValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"message": "Director Data with errors!!!",
                                  "errors": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director = Director.objects.create(
            name=request.data.get('name')
        )
        director.save()
        return Response(data={"message": "Director created successfully!"},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def one_director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    if request.method == "GET":
        return Response(data=DirectorListSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(data={"message": "Director removed successfully!"},
                        status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data={"message": "Director updated successfully!",
                              "director": DirectorListSerializer(director).data})

@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieListSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MoviesBaseValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration'),
            director_id=request.data.get('director')
        )
        movie.save()
        return Response(data={"message": "Movie created successfully!"},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def one_movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    if request.method == 'GET':
        return Response(data=MovieListSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={"message": "Movie removed successfully!"},
                        status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MoviesBaseValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"message": "Director Data with errors!!!",
                                  "errors": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie.title = request.data.get('title'),
        movie.description = request.data.get('description'),
        movie.duration = request.data.get('duration'),
        movie.save()

        return Response(data={
                            "message": 'Movie updated successfully',
                            'movie': MovieListSerializer(movie).data
                        })

@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MoviesBaseValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.create(
            text=request.data.get('text'),
            movie_id=request.data.get('movie'),
            stars=request.data.get('stars')
        )
        review.save()
        return Response(data={"message": "Review created successfully!"},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def one_review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found'})
    if request.method == 'GET':
        return Response(ReviewListSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data={"message": "Review removed successfully!"},
                        status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':

        review.text = request.data.get('text'),
        review.save()

        return Response(data={
            "message": 'Review updated successfully',
            'review': ReviewListSerializer(review).data
        })

@api_view(['GET'])
def movies_reviews_view(request):
    movies_reviews = Movie.objects.all()
    data = MovieReviewListSerializer(movies_reviews, many=True).data
    return Response(data=data)



