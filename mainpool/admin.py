from django.contrib import admin

# Register your models here.
from .models import WalletAddress


@admin.register(WalletAddress)

class WalletAddressAdmin(admin.ModelAdmin):
    list_display = ['btc_wallet', 'litecoin_wallet', 'busd_wallet']