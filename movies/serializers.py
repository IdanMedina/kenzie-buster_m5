from rest_framework import serializers
from .models import Movie, MovieRating, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, default=None, required=False)
    rating = serializers.ChoiceField(
        choices=MovieRating.choices, default=MovieRating.G, required=False)
    synopsis = serializers.CharField(default=None, required=False)
    added_by = serializers.EmailField(read_only=True, source="user.email")

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    title = serializers.EmailField(read_only=True, source="movie.title")
    buyed_by = serializers.EmailField(read_only=True, source="order.email")
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data: dict) -> Movie:
        return MovieOrder.objects.create(**validated_data)
