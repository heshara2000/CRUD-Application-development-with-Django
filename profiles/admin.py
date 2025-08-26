from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'age', 'created_at')
    search_fields = ('name', 'email', 'phone_number')