from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import PhoneToken, User

User = get_user_model()


class UserSerializer(ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'phone_number', 'nickname',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class PhoneTokenCreateSerializer(ModelSerializer):
    phone_number = serializers.CharField(validators=PhoneNumberField().validators)

    class Meta:
        model = PhoneToken
        fields = ('phone_number','nickname', 'password','otp')


class PhoneTokenUser(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class PhoneTokenValidateSerializer(ModelSerializer):
    pk = serializers.IntegerField()
    otp = serializers.CharField(max_length=40)

    class Meta:
        model = PhoneToken
        fields = ('pk', 'otp','nickname', 'password')
