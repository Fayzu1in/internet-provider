from rest_framework import serializers

from .models import Plan, Coverage, Callback, Offer, TopProvider


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
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
        model = TopProvider
        fields = '__all__'