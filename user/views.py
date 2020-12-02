from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView

from user.services.authentication import get_or_create_token
from user.models.customer import Customer
from user.serializers import LoginSerializer, CustomerSerializer, CustomerRegisterSerializer, UserSerializer


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username, password = data.get('username', ''), data.get('password', '')
        customer = get_object_or_404(Customer.objects.all(), username=username)

        if not check_password(password, customer.password):
            raise ValidationError(
                'wrong password',
                code=HTTP_403_FORBIDDEN
            )

        token = get_or_create_token(customer)
        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_200_OK
        )


class RegisterView(APIView):

    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()

        token = get_or_create_token(customer)
        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_201_CREATED
        )


class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(
            serializer.data
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(
            serializer.data
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
