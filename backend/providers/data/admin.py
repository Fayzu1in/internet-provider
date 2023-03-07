from django.contrib import admin
from .models import Plan, Coverage

@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'speed', 'price']


@admin.register(Coverage)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['district', 'street']
