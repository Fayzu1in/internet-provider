from rest_framework import serializers

from .models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class CoverageSerializer(serializers.ModelSerializer):
    providers = serializers.SerializerMethodField()

    def get_providers(self, obj):
        return [{'id': provider.id, 'name': provider.name} for provider in obj.providers.all()]

    class Meta:
        model = Coverages
        fields = '__all__'


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class TopProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProviders
        fields = '__all__'
        pass


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllProviders
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
