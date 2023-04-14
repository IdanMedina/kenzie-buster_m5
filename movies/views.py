from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsEmployee


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.user)
        serializer.save(user=request.user)
        serializer.save(added_by=request.user["email"])

        return (serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movie_set = Movie.objects.all()
        serializer = MovieSerializer(movie_set, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class MovieInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployee]

    def get(self, request: Request, movie_id: int) -> Response:
        get_movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(get_movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        get_movie = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(request, get_movie)
        get_movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
