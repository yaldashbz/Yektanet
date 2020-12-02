from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer, CharField, ModelSerializer

from user.models.customer import Customer


class LoginSerializer(Serializer):
    username = CharField()
    password = CharField()

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class CustomerRegisterSerializer(ModelSerializer):
    def validate_password(self, password):
        return make_password(password)

    class Meta:
        model = Customer
        fields = [
            'username',
            'password'
        ]


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'username',
            'balance'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
