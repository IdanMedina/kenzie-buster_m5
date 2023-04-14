from rest_framework import serializers
from .models import Movie, MovieRating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, default=None, required=False)
    rating = serializers.ChoiceField(
        choices=MovieRating.choices, default=MovieRating.G, required=False)
    synopsis = serializers.CharField(default=None, required=False)
    added_by = serializers.EmailField(read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
