from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser 

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'phone_number']