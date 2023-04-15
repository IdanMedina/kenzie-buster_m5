from django.urls import path
from .views import MovieView, MovieInfoView, MovieOrderView


urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieInfoView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
