from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class TierOne(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    investors_id = models.CharField(max_length=50, blank=True, null=True)
    wallet_address = models.CharField(max_length=500, blank=True, null=True)
    coin_used = models.CharField(max_length=20, blank=True, null=True)
    amount_invested = models.IntegerField( blank=True, null=True)
    roi = models.IntegerField( blank=True, null=True)
    date_of_investment = models.DateTimeField(auto_now_add=True)
    date_of_maturity = models.CharField(max_length=50, blank=True, null=True)
