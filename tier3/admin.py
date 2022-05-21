# Register your models here.
from django.contrib import admin
from .models import TierThree

@admin.register(TierThree)
class TierThreeAdmin(admin.ModelAdmin):
    list_display = ['investor', 'coin_used', 'roi','amount_invested', 'date_of_investment']