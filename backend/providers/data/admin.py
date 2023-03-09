from django.contrib import admin
from .models import Plan, Coverage, Callback

@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['provider','title', 'name', 'speed', 'price']
    search_fields = ['provider','title', 'name', 'speed', 'price']

@admin.register(Coverage)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['district', 'street']


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
