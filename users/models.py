from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
import pandas as pd

# Create your models here.
User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)
    tradeID = models.CharField(max_length=100, unique=True, blank=True)
    email = models.EmailField(unique=True)
    btc_address = models.CharField(max_length=500, blank=True, null=True)
    litecoin_address = models.CharField(max_length=500, null=True, blank=True)
    busd_address = models.CharField(max_length=500, blank=True, null=True)
    wallet_created = models.BooleanField(default=False)
    phone_number = PhoneNumberField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "phone_number",
        "password",
    ]

    def __str__(self):
        return self.email
