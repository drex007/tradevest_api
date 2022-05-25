from datetime import timedelta, date
from pyexpat import model
from django.db import models
from django.conf import settings
import time
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

import pandas as pd

# Create your models here.
User = settings.AUTH_USER_MODEL


class TierOne(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    investors_id = models.CharField(max_length=50, blank=True, null=True)
    transction_id = models.CharField(max_length=100, unique=True, blank=True)
    wallet_address = models.CharField(max_length=500, blank=True, null=True)
    coin_used = models.CharField(max_length=20, blank=True, null=True)
    amount_invested = models.IntegerField(blank=True, null=True)
    roi = models.IntegerField(blank=True, null=True)
    earnings = models.IntegerField(blank=True, default=0)
    date_of_investment = models.DateTimeField(auto_now_add=True)
    date_confirmed = models.DateTimeField(max_length=50, blank=True, null=True)
    date_of_maturity = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        total = self.roi + (self.amount_invested)
        if self.status == True and self.earnings < total:
            if self.date_confirmed == None:
                date = timezone.now()
                self.date_confirmed = pd.to_datetime(date).date()

                self.date_of_maturity = self.date_confirmed + timedelta(days=6)
            self.incrementEarns()

        super(TierOne, self).save(*args, **kwargs)

    def incrementEarns(self):
        print("Hi")
        self.earnings += self.roi + self.amount_invested
        print(self.earnings)
