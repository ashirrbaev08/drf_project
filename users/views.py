from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from . serializers import UserRegistrationSerializer,UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from . models import ConfirmCode
from rest_framework.generics import ListAPIView




@api_view(['POST'])
def user_confirm_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(
        status=status.HTTP_200_OK, 
        data={'message': 'Аккаунт успешно активирован!'}
    )


@api_view(['POST'])
def authorization_api_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response(data={'key':token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']


    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False)

    generated_code = str(random.randint(100000, 999999))
    ConfirmCode.objects.create(
        user=user,         
        code=generated_code
    )

    return Response(
        status=status.HTTP_201_CREATED,
        data={'user_id': user.id}
    )