from django.contrib import admin
from .models import *
from django.contrib import admin
from django.utils.safestring import mark_safe

admin.site.site_header = 'internetBor'
admin.site.index_title = 'Admin Panel'


@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['provider', 'title', 'position', 'speed', 'price', 'created']
    list_filter = ['provider']
    search_fields = ['provider', 'title', 'name', 'speed', 'price', 'position']


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created', 'status']
    list_filter = ['status', 'created']
    search_fields = ['status']


@admin.register(Coverages)
class CoverageAdmin(admin.ModelAdmin):
    list_display = ['city', 'district', 'street', 'created', 'edited']
    search_fields = ['city', 'district', 'street']
    list_filter = ['city', 'district']
    exclude = ['providers']


admin.site.register(Offer)


@admin.register(TopProviders)
class TopProviderAdmin(admin.ModelAdmin):
    list_display = ['provider']


@admin.register(AllProviders)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position','display_pic', 'is_published']
    list_filter = ['is_published', 'position']
    search_fields = ['name', 'info']

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


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created', 'published']
#     list_filter = ['published']
#     search_fields = ['title', 'text']


@admin.register(Adressless)
class AdresslessAdmin(admin.ModelAdmin):
    list_display = ['phone', 'status', 'created']
    list_filter = ['status', 'created']
    search_fields = ['phone']


@admin.register(QuestionAndAnswers)
class QuestionAndAnswersAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'created', 'updated', 'id']
