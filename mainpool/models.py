from django.db import models

# Create your models here.


class WalletAddress(models.Model):
    btc_wallet = models.CharField(max_length=500, blank=True, null=True, default= "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
    litecoin_wallet = models.CharField(max_length=500, blank=True, null=True,default= "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
    busd_wallet = models.CharField(max_length=500, blank=True, null=True, default= "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
    