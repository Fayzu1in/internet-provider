from django.contrib import admin
from .models import Plan, Coverage, Callback, Offer, TopProvider
from django.contrib import admin

admin.site.site_header = 'Providers Admin panel'
admin.site.index_title = 'Welcome to My Custom Admin Panel'


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



admin.site.register(Offer)



@admin.register(TopProvider)
class TopProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
