from django.db import models
from users.models import User


class MovieRating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=MovieRating.choices, default=MovieRating.G,
        null=True)
    synopsis = models.TextField(null=True, default=None)
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, default=None)
