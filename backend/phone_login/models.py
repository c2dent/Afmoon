from __future__ import unicode_literals

import datetime
from datetime import timezone
import hashlib
import os

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.db import models, transaction
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from sendsms.message import SmsMessage
from twilio.rest import Client

account_sid = "AC560c1472993104ce842be8d400d12402"
auth_token  = "8c4e3247cdf3744a49160bf3acc9af64"
client = Client(account_sid, auth_token)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password,nickname, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not phone_number:
            raise ValueError('The given username must be set')
        try:
            with transaction.atomic():
                user = self.model(phone_number=phone_number, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise


    def create_user(self, phone_number, password=None, nickname=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password,nickname, **extra_fields)

    def create_superuser(self,  phone_number, password, nickname,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password=password, nickname=nickname,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=40, unique=True, default='+79889155078')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    last_visit = models.DateTimeField(auto_now=True)
    nickname = models.CharField(max_length=40,null=True, blank=True, default='Nickname')
    avatar = models.ImageField(blank=True, null=True, upload_to='images', default='images/user.png')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['nickname']
    objects = UserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True



class PhoneToken(models.Model):
    phone_number = models.CharField(max_length=16, default='+79889155078')
    nickname = models.CharField(max_length=40 , blank=True, null=True, default='Nickname')
    password = models.CharField(max_length=16, default='Nickname')
    otp = models.CharField(max_length=40, editable=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    attempts = models.IntegerField(default=0)
    used = models.BooleanField(default=False)

    class Meta:
        verbose_name = "OTP Token"
        verbose_name_plural = "OTP Tokens"

    def __str__(self):
        return "{} - {}".format(self.phone_number, self.otp)

    @classmethod
    def create_otp_for_number(cls, phone_number, nickname,password):
        # The max otps generated for a number in a day are only 10.
        # Any more than 10 attempts returns False for the day.
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        otps = cls.objects.filter(phone_number=phone_number, timestamp__range=(today_min, today_max))
        if otps.count() <= getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10):
            otp = cls.generate_otp(length=getattr(settings, 'PHONE_LOGIN_OTP_LENGTH', 6))
            phone_token = PhoneToken(phone_number=phone_number, nickname=nickname,password=password, otp=otp)
            phone_token.save()
            from_phone = getattr(settings, 'SENDSMS_FROM_NUMBER')
            message = client.messages.create(
                body=render_to_string(
                   "otp_sms.txt",
                    {"otp": otp, "id": phone_token.id}
                ),
                from_= from_phone,
                to= [phone_number]
            )
            #message.send()
            return otp
        else:
            return False

    @classmethod
    def generate_otp(cls, length=6):
        hash_algorithm = getattr(settings, 'PHONE_LOGIN_OTP_HASH_ALGORITHM', 'sha256')
        m = getattr(hashlib, hash_algorithm)()
        m.update(getattr(settings, 'SECRET_KEY', None).encode('utf-8'))
        m.update(os.urandom(16))
        otp = str(int(m.hexdigest(), 16))[-length:]
        return otp
