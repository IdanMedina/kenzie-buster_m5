from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

username_error = "username already taken."
email_error = "email already registered."


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField(
        validators=[UniqueValidator(User.objects.all(), username_error)]
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[UniqueValidator(User.objects.all(), email_error)]
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False, required=False)
    is_superuser = serializers.BooleanField(
        default=False, read_only=True, required=False)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
        return instance
