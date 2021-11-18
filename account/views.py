from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from utilities import response_writer

from .serializers import LoginSerializer, SignUpSerializer, UpdatePasswordSerializer
from .utilities import get_access_token, get_refresh_token

# Create your views here.


class AuthAPIView(APIView):
    permission_classes = (AllowAny,)

    # For SignUp
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User = get_user_model()
        user = User.objects.filter(
            username=serializer.validated_data["username"]
        ).exists()

        if user:
            response = response_writer("error", None, 409, "User already exists")
            return Response(response, status=status.HTTP_409_CONFLICT)

        serializer.save()
        access_token = get_access_token(serializer.validated_data["username"])
        refresh_token = get_refresh_token(serializer.validated_data["username"])

        response = response_writer(
            "success",
            {"access_token": access_token, "refresh_token": refresh_token},
            200,
            "Signup successful",
        )
        return Response(response, status=status.HTTP_200_OK)

    # For login
    def get(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User = get_user_model()
        user = User.objects.filter(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user.exists():
            response = response_writer("error", None, 404, "Incorrect combination of credentials")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        access_token = get_access_token(serializer.validated_data["username"])
        refresh_token = get_refresh_token(serializer.validated_data["username"])

        response = response_writer(
            "success",
            {"access_token": access_token, "refresh_token": refresh_token},
            200,
            "Login successful",
        )
        return Response(response, status=status.HTTP_200_OK)


class UserUpdateDeleteAPIView(APIView):
    def patch(self, request):
        User = get_user_model()
        user = User.objects.get(username=request.user.username)

        serializer = UpdatePasswordSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = response_writer(
            "success", None, 200, "Password updated successfully"
        )
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):
        User = get_user_model()
        user = User.objects.get(username=request.user.username)

        user.delete()

        response = response_writer(
            "success", None, 200, "User profile deleted successfully"
        )
        return Response(response, status=status.HTTP_200_OK)
