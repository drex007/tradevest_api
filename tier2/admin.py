# Register your models here.
from django.contrib import admin
from .models import TierTwo

@admin.register(TierTwo)
class TierTwoAdmin(admin.ModelAdmin):
    list_display = ['investor', 'coin_used', 'roi','amount_invested', 'date_of_investment']