# Register your models here.
from django.contrib import admin
from .models import TierOne

@admin.register(TierOne)
class TierOneAdmin(admin.ModelAdmin):
    list_display = ['investor', 'coin_used', 'roi','amount_invested', 'date_of_investment', 'date_of_maturity']