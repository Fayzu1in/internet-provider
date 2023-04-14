from rest_framework import serializers

from .models import *


class PlanSerializer(serializers.ModelSerializer):
    provider_name = serializers.SerializerMethodField()
    provider_info = serializers.SerializerMethodField()
    provider_picture = serializers.SerializerMethodField()

    def get_provider_name(self, obj):
        return obj.provider.name

    def get_provider_info(self, obj):
        return obj.provider.info

    def get_provider_picture(self, obj):
        return obj.provider.picture.url

    class Meta:
        model = Plan
        fields = [
            'id',
            'provider_id',
            'provider_name',
            'provider_info',
            'provider_picture',
            'name',
            'title',
            'speed',
            'price',
            'tech',
            'limit',
            'day',
            'night',
            'info',
            'abonents',
            'is_hot'
        ]


class CoverageSerializer(serializers.ModelSerializer):
    providers = serializers.SerializerMethodField()

    def get_providers(self, obj):
        # return [{'provider_id': provider.id, 'provider_name': provider.name, 'provider_picture': provider.picture.url, 'provider_info': provider.info, 'provider_best': provider.best_plans} for provider in obj.providers.all()]
        provider_data = []
        for provider in obj.providers.all():
            if provider.is_published:
                provider_dict = {
                    'provider_id': provider.id,
                    'provider_name': provider.name,
                    'provider_picture': provider.picture.url,
                    'provider_info': provider.info,
                    'provider_best': [],
                    'is_published': provider.is_published,

                }
                for plan in provider.best_plans.all():
                    provider_dict['provider_best'].append({
                        'plan_id': plan.id,
                        'plan_name': plan.title,
                        'plan_speed': plan.speed,
                        'plan_limit': plan.limit,
                        'plan_price': plan.price,
                        'plan_info': plan.info,
                        'provider_id': plan.provider.id,
                        'provider_name': plan.provider.name,
                        'provider_info': plan.provider.info,
                        'provider_picture': plan.provider.picture.url,
                        'tech': plan.tech,
                        'limit': plan.limit,
                        'day': plan.day,
                        'night': plan.night,
                        'info': plan.info,
                        'abonents': plan.abonents,
                        'is_hot': plan.is_hot
                        # Add more plan fields as needed
                    })
                provider_data.append(provider_dict)
        return provider_data

    class Meta:
        model = Coverages
        fields = '__all__'


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    plans = serializers.SerializerMethodField()

    def get_plans(self, obj):
        return [
            {'plan_id': plan.id,
             'provider_name': plan.provider.name,
             'provider_picture': plan.provider.picture.url,
             'name': plan.name,
             'title': plan.title, 'price': plan.price,
             'tech': plan.tech,
             'day': plan.day,
             'night': plan.night,
             'speed': plan.speed,
             'limit': plan.limit
             } for plan in obj.plans.all() if plan.provider.is_published
        ]

    class Meta:
        model = Offer
        fields = '__all__'


class TopProviderSerializer(serializers.ModelSerializer):
    provider_name = serializers.SerializerMethodField()
    provider_picture = serializers.SerializerMethodField()

    def get_provider_picture(self, obj):
        return obj.provider.picture.url

    def get_provider_name(self, obj):
        return obj.provider.name

    class Meta:
        model = TopProviders
        fields = [
            'id',
            'provider_id',
            'provider_name',
            'provider_picture',
            'text',
        ]

    def to_representation(self, instance):
        if instance.provider.is_published:
            return super().to_representation(instance)
        else:
            return None


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllProviders
        fields = [
            'id',
            'name',
            'picture',
            'info',
            'is_published',
        ]

    def to_representation(self, provider):
        if provider.is_published:
            return super().to_representation(provider)
        else:
            return None


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = '__all__'
