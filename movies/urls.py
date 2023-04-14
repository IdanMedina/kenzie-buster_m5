from django.urls import path
from .views import MovieView, MovieInfoView


urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieInfoView.as_view())
]
