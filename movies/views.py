from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from .permissions import IsEmployee


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployee]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movie_set = Movie.objects.all()
        serializer = MovieSerializer(movie_set, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class MovieInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployee]

    def get(self, request: Request, movie_id: int) -> Response:
        get_movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(get_movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        get_movie = get_object_or_404(Movie, pk=movie_id)
        get_movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(order=request.user, movie=movie_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)
