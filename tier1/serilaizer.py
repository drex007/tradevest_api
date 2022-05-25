from hmac import trans_36
import time
from rest_framework import serializers
from .models import TierOne
from datetime import date, timedelta
from users.models import CustomUser
from .models import TierOne
from random import randint
from django.utils import timezone
import pandas as pd
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from apscheduler.schedulers.background import BackgroundScheduler

import schedule


class TierOneSeriealizer(serializers.ModelSerializer):
    coin_used = serializers.CharField()
    amount_invested = serializers.IntegerField()
    wallet_address = serializers.CharField()
    # email = serializers.CharField(read_only=True)

    class Meta:
        model = TierOne
        fields = "__all__"
        extra_kwargs = {
            "roi": {"read_only": True},
            "investors_id": {"read_only": True},
            "earnings": {"read_only": True},
            "investor": {"read_only": True},
            "status": {"read_only": True},
            "date_of_investment": {"read_only": True},
            "date_of_maturity": {"read_only": True},
            "date_confirmed": {"read_only": True},
            "transction_id": {"read_only": True},
        }

    def create(self, validated_data):
        request = self.context  # Receives the context as request from the view file

        date_now = timezone.now()
        date_created = pd.to_datetime(date_now).date()

        roi = 0.2 * validated_data.get("amount_invested")
        trans = randint(000000, 999999)
        trans_id = f"Trans{trans}"

        transaction = TierOne.objects.create(
            investor=request.user,
            transction_id=trans_id,
            amount_invested=validated_data.get("amount_invested"),
            investors_id=request.user.tradeID,
            roi=roi,
            date_of_investment=date_created,
            coin_used=validated_data.get("coin_used"),
            wallet_address=validated_data.get("wallet_address"),
            # date_of_maturity=date_of_maturity,
        )

        transaction.save()
        return transaction


class GetAllTransactionSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = TierOne
        fields = "__all__"
