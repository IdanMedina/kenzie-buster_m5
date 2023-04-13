from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .models import User
from .serializers import UserSerializer


class UserView(APIView):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["is_employee"] is True:
            serializer.validated_data["is_superuser"] = True

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
