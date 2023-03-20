from rest_framework import serializers

from .models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class CoverageSerializer(serializers.ModelSerializer):
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
