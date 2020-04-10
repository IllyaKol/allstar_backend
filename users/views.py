import jwt

from django.contrib.auth import user_logged_in
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.serializers import jwt_payload_handler

from allstar import settings
from allstar import urls
from .models import User
from .utils import get_user_data
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    email = request.data['email']
    password = request.data['password']
    if not (email and password):
        response = {'error': 'Please provide a email and a password'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(email=email)

        if not user.check_password(password):
            res = {'error': 'Incorrect password'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)

        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_details = get_user_data(user)
            user_details['token'] = token
            user_logged_in.send(sender=user.__class__,
                                request=request,
                                user=user)
            urls.redis_connection.set(
                name=f'{settings.REDIS_PROCESSING_KEY}{user.id}',
                value=token,
                ex=settings.TOKEN_EXPIRE
            )
            return Response(user_details, status=status.HTTP_200_OK)
        except Exception as e:
            raise e
    except ObjectDoesNotExist:
        res = {'error': 'Incorrect email'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        token = request.auth

        user_token = urls.redis_connection.get(
            f'{settings.REDIS_PROCESSING_KEY}{user_id}'
        )
        if user_token and user_token == token:
            return True
        return False


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsTokenValid,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def logout(request):
    user_id = request.user.id
    urls.redis_connection.delete(f'{settings.REDIS_PROCESSING_KEY}{user_id}')
    response = {'success': True}
    return Response(response, status=status.HTTP_200_OK)
