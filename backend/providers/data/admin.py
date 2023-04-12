from django.contrib import admin
from .models import *
from django.contrib import admin
from django.utils.safestring import mark_safe

admin.site.site_header = 'Providers Admin panel'
admin.site.index_title = 'Welcome to My Custom Admin Panel'


@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['provider', 'title', 'name', 'speed', 'price']
    list_filter = ['provider']
    search_fields = ['provider', 'title', 'name', 'speed', 'price']


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created', 'status']
    list_filter = ['status']
    search_fields = ['status']


@admin.register(Coverages)
class CoverageAdmin(admin.ModelAdmin):
    list_display = ['city', 'district', 'street']
    search_fields = ['city', 'district','street']
    list_filter = ['city']


admin.site.register(Offer)


@admin.register(TopProviders)
class TopProviderAdmin(admin.ModelAdmin):
    list_display = ['provider']


@admin.register(AllProviders)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_pic', 'info'[:10]]


    def display_pic(self, obj):
        return mark_safe('<img src="/api%s"  width="50" height="50>"' % obj.picture.url)

    display_pic.allow_tags = True
    display_pic.short_description = 'Picture'

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "plan":
    #         provider_id = request.resolver_match.args[0]
    #         if provider_id:
    #             provider = AllProviders.objects.get(pk=provider_id)
    #             kwargs["queryset"] = provider.best_plans.all()
    #         else:
    #             kwargs["queryset"] = Plan.objects.none()
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)



@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'is_admin', 'logged']
    list_filter = ['is_admin']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'published']
    list_filter = ['published']
    search_fields = ['title', 'text']


