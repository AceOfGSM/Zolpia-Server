from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _
import jwt
from django.contrib.auth.hashers import make_password


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "name")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=128)
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user is None:
            msg = _("User instance not exists")
            raise serializers.ValidationError(msg)

        payload = {
            "email": user.email,
            "name": user.name,
            "is_active": user.is_active,
        }
        token = utils.jwt_encode_handler(payload)  # token 만들고

        return user, token  # user, token 반환


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "name")
