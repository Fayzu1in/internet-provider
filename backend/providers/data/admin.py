from django.contrib import admin
from .models import *
from django.contrib import admin
from django.utils.safestring import mark_safe

admin.site.site_header = 'Providers Admin panel'
admin.site.index_title = 'Welcome to My Custom Admin Panel'


@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['provider', 'title', 'name', 'speed', 'price']
    search_fields = ['provider', 'title', 'name', 'speed', 'price']


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created']
    list_filter = ['status']
    search_fields = ['status']


@admin.register(Coverages)
class CoverageAdmin(admin.ModelAdmin):
    list_display = ['district', 'street']
    search_fields = ['district', 'street']
    list_filter = ['district']


admin.site.register(Offer)


@admin.register(TopProviders)
class TopProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'provider', 'display_pic']

    def display_pic(self, obj):
        return mark_safe('<img src="%s" width="50" height="50"' % obj.logo.url)

    display_pic.allow_tags = True
    display_pic.short_description = 'Logo'


@admin.register(AllProviders)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ['name', 'info'[:10]]


@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'is_admin', 'logged']
