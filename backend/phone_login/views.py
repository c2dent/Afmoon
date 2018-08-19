from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import datetime, jwt
from catalog.models import CustomUser
from catalog.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.signals import user_logged_in
from .models import PhoneToken
from .serializers import PhoneTokenCreateSerializer, ChangePasswordSerializer
import hashlib, os
from django.template.loader import render_to_string

# from .backends.phone_backend import PhoneBackend

from .models import PhoneToken, User
from .serializers import (
    PhoneTokenCreateSerializer, PhoneTokenValidateSerializer, UserSerializer
)
from .utils import user_detail
from twilio.rest import Client

account_sid = "AC560c1472993104ce842be8d400d12402"
auth_token  = "8c4e3247cdf3744a49160bf3acc9af64"
client = Client(account_sid, auth_token)
    
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class GenerateOTP(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenCreateSerializer

    def post(self, request, format=None):
        phone_number = request.data.get("phone_number")
        otp = create_otp_number(phone_number)
        if otp :
            phone_token = {
            'phone_number': request.data.get('phone_number'),
            'otp' : otp,
            'password': request.data.get('password'),
            'nickname': request.data.get('nickname'),
            } 
            # phone_token.update({'otp': token})
            serializer = PhoneTokenCreateSerializer(data= phone_token)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(phone_number, status=status.HTTP_201_CREATED)
    


class Registration(CreateAPIView):
    timestamp_difference = datetime.datetime.now() - datetime.timedelta(minutes=getattr(settings, 'PHONE_LOGIN_MINUTES', 10))
    permission_classes = (AllowAny,)

    def post(self, request):
        timestamp_difference = datetime.datetime.now() - datetime.timedelta(minutes=getattr(settings, 'PHONE_LOGIN_MINUTES', 10))
        try:
            phone_number = request.data['phone_number']
            otp = request.data['otp']

            phone_token = PhoneToken.objects.get(
                phone_number=phone_number,
                otp=otp,
                timestamp__gte=timestamp_difference
                )
            user = {
            phone_number : phone_token.phone_number,
            # 'password' : phone_token.password,
            'nickname' : phone_token.nickname
            }

        except Exception as e :
            raise e

        # user = request.data
        serializer = CustomUserSerializer(data=user)
        serializer.set_password(phone_token.password)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([AllowAny,])
def authenticate_user(request):
    try:
        phone_number = request.data['phone_number']
        password = request.data['password']
        try:
            user = CustomUser.objects.get(phone_number=phone_number, password=password)
        except CustomUser.DoesNotExist:
            user = None

        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                # user_details['name'] = "%s %s" % (user.nickname)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a phone_number and a password'}
        return Response(res)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = CustomUser.objects.get(pk = self.request.user.pk)
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_otp_number(phone_number):
    otp = generate_otp(length=getattr(settings, 'PHONE_LOGIN_OTP_LENGTH', 6))
    from_phone = getattr(settings, 'SENDSMS_FROM_NUMBER')
    message = client.messages.create(
        body=render_to_string(
            "otp_sms.txt",
            {"otp": otp, "phone_number": phone_number}
            ),
        from_= from_phone,
        to= [phone_number]
        )
    return otp

def generate_otp(length=6):
    hash_algorithm = getattr(settings, 'PHONE_LOGIN_OTP_HASH_ALGORITHM', 'sha256')
    m = getattr(hashlib, hash_algorithm)()
    m.update(getattr(settings, 'SECRET_KEY', None).encode('utf-8'))
    m.update(os.urandom(16))
    otp = str(int(m.hexdigest(), 16))[-length:]
    return otp