from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        read_only_fields = ["username"]
