from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from . models import ConfirmCode



class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=155)
    password = serializers.CharField()


    def validate_username(self,username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')

class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()

    def validate(self,attrs):
        username = attrs.get('username')
        code = attrs.get('code')
        try:
            user = User.objects.get(username=username)
            confirm_empty = ConfirmCode.objects.get(user=user, code=code)
            user.is_active = True
            user.save()
            confirm_empty.delete()
        except (User.DoesNotExist, ConfirmCode.DoesNotExist):
            raise ValidationError('Неверный код подтверждения или пользователь не найден!')
        return attrs
