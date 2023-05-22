from rest_framework import serializers
import re 
from .models import *


class PlanSerializer(serializers.ModelSerializer):
    provider_name = serializers.SerializerMethodField()
    provider_info = serializers.SerializerMethodField()
    provider_picture = serializers.SerializerMethodField()
    provider_position = serializers.SerializerMethodField()
    # provider = serializers.SerializerMethodField()

    # def get_provider(self, obj):
    #     provider = AllProviders.objects.get(id=obj.provider.id)
    #     if provider.is_published == False:
    #         return None
        
    def get_provider_name(self, obj):
        return obj.provider.name

    def get_provider_info(self, obj):
        return obj.provider.info

    def get_provider_picture(self, obj):
        return obj.provider.picture.url
    
    def get_provider_position(self, obj):
        return obj.provider.position
    
    
    

    class Meta:
        model = Plan
        fields = [
            'id',
            # 'provider',
            'provider_id',
            'provider_name',
            'provider_info',
            'provider_picture',
            'provider_position',
            'position',
            'name',
            'title',
            'speed',
            'price',
            'tech',
            'limit',
            'day',
            'daily_speed_time',
            'night',
            'nightly_speed_time',
            'info',
            'abonents',
            'is_hot',
            'router',
            'router_text',
            'tv',
            'tv_text',
            'cabel',
            'cabel_text',
            'more_info',
        ]


class CoverageSerializer(serializers.ModelSerializer):
    providers = serializers.SerializerMethodField()
    houses = serializers.SerializerMethodField()
    freelink_houses = serializers.SerializerMethodField()
    comnet_houses = serializers.SerializerMethodField()
    sarkor_houses = serializers.SerializerMethodField()
    ars_inform_houses = serializers.SerializerMethodField()
    uzonline_houses = serializers.SerializerMethodField()
    city_net_houses = serializers.SerializerMethodField()
    gals_houses = serializers.SerializerMethodField()
    spectr_houses = serializers.SerializerMethodField()
    optikom_houses = serializers.SerializerMethodField()

    def get_providers(self, obj):
        # return [{'provider_id': provider.id, 'provider_name': provider.name, 'provider_picture': provider.picture.url, 'provider_info': provider.info, 'provider_best': provider.best_plans} for provider in obj.providers.all()]
        provider_data = []
        for provider in obj.providers.all():
            if provider.is_published:
                #? for production
                provider_dict = {
                    'provider_id': provider.id,
                    'provider_name': provider.name,
                    'provider_picture': provider.picture.url,
                    'provider_info': provider.info,
                    'provider_best': [],
                    'is_published': provider.is_published,
                }
                for plan in provider.best_plans.all():
                    provider_dict['provider_best'].append(
                        {
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
                            'provider_position': plan.provider.position,
                            'tech': plan.tech,
                            'limit': plan.limit,
                            'day': plan.day,
                            'night': plan.night,
                            'info': plan.info,
                            'abonents': plan.abonents,
                            'is_hot': plan.is_hot,
                            'router': plan.router
                            # Add more plan fields as needed
                        })
                provider_data.append(provider_dict)

                # # #? for import 
                # provider_data.append(*{provider.name})
            else:
                pass

        if len(provider_data) != 0:
            return provider_data
        else:
            return None
        

    def get_houses(self, obj):
        try:
            if ',' in obj.houses:
                coma = obj.houses.split(',')
                # coma = sorted(coma)
                return coma
            elif obj.houses[0] == '[':
                return sorted(obj.houses[1:-1].split(', '))
                
            else: 
                space = obj.houses.split(' ')
                # space = sorted(space)
                return space
        except:
            return []

    def get_freelink_houses(self, obj):
        try:
            if ',' in obj.freelink_houses:
                coma = obj.freelink_houses.split(',')
                # coma = sorted(coma)
                return coma
            elif obj.freelink_houses[0] == '[':
                return sorted(obj.freelink_houses[1:-1].split(', '))
            else: 
                space = obj.freelink_houses.split(' ')
                # space = sorted(space)
                return space
        except:
            return []
    
    def get_comnet_houses(self, obj):
        try:
            if ',' in obj.comnet_houses:
                coma = obj.comnet_houses.split(',')
                # coma = sorted(coma)
                return coma
            elif obj.comnet_houses[0] == '[':
                return sorted(obj.comnet_houses[1:-1].split(', '))
            else: 
                space = obj.comnet_houses.split(' ')
                # space = sorted(space)
                return space
        except:
            return []
        
    def get_sarkor_houses(self, obj):
        try:
            if ',' in obj.sarkor_houses:
                coma = obj.sarkor_houses.split(',')
                # coma = sorted(coma)
                return coma
            elif obj.sarkor_houses[0] == '[':
                return obj.sarkor_houses[1:-1].split(', ')
            else: 
                space = obj.sarkor_houses.split(' ')
                # space = sorted(space)

                return space

        except:
            return []
   
        
    def get_ars_inform_houses(self, obj):
        try:
            if ',' in obj.ars_inform_houses:
                coma = obj.ars_inform_houses.split(',')
                # coma = sorted(coma)

                return coma
            elif obj.ars_inform_houses[0] == '[':
                return obj.ars_inform_houses[1:-1].split(', ')
            else: 
                space = obj.ars_inform_houses.split(' ')
                # space = sorted(space)

                return space
        
        except:
            return []
    
    def get_uzonline_houses(self, obj):
        try:
            if ',' in obj.uzonline_houses:
                coma = obj.uzonline_houses.split(',')
                # coma = sorted(coma)

                return coma
            elif obj.uzonline_houses[0] == '[':
                return obj.uzonline_houses[1:-1].split(', ')
            else: 
                space = obj.uzonline_houses.split(' ')
                # space = sorted(space)

                return space
        except:
            return []
    
    def get_city_net_houses(self, obj):
        try:
            if ',' in obj.city_net_houses:
                coma = obj.city_net_houses.split(',')
                # coma = sorted(coma)

                return coma
            elif obj.city_net_houses[0] == '[':
                return obj.city_net_houses[1:-1].split(', ')
            else: 
                space = obj.city_net_houses.split(' ')
                # space = sorted(space)

                return space
        except:
            return []
    
    def get_gals_houses(self, obj):
        try:
            if ',' in obj.gals_houses:
                coma = obj.gals_houses.split(',')
                # coma = sorted(coma)

                return coma
            elif obj.gals_houses[0] == '[':
                return obj.gals_houses[1:-1].split(', ')
            else: 
                space = obj.gals_houses.split(' ')
                # space = sorted(space)
                return space
        except:
            return []
    
    def get_spectr_houses(self, obj):
        try:
            if ',' in obj.spectr_houses:
                coma = obj.spectr_houses.split(',')
                # coma = sorted(coma)

                return coma
            elif obj.spectr_houses[0] == '[':
                return obj.spectr_houses[1:-1].split(', ')
            else: 
                space = obj.spectr_houses.split(' ')
                # space = sorted(space)
                return space
        except:
            return []
        

    def get_optikom_houses(self, obj):
        try:
            if ',' in obj.optikom_houses:
                coma = obj.optikom_houses.split(',')
                # coma = sorted(coma)

                return coma
            elif obj.optikom_houses[0] == '[':
                return obj.optikom_houses[1:-1].split(', ')
            else: 
                space = obj.optikom_houses.split(' ')
                # space = sorted(space)
                return space
        except:
            return []


    class Meta:
        model = Coverages
        fields = [
            'city',
            'district',
            'street',
            'providers',
            'houses',
            "sarkor_houses",
            "comnet_houses",
            "uzonline_houses",
            "freelink_houses",
            "ars_inform_houses",
            "city_net_houses",
            "gals_houses",
            "spectr_houses",
            'optikom_houses'
        ]


class CoverageCitiesSerializer(serializers.ModelSerializer):

    houses = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    def extract_alphanumeric_parts(s):
        parts = re.findall(r'(\d+|\D+)', s)
        return [int(p) if p.isdigit() else p for p in parts]


    def get_houses(self, obj):
        try:
            if 'сектор' in obj.houses:
                return obj.houses 
            if ',' in obj.houses:
                coma = obj.houses.split(',')
                coma = set(coma)
                coma = list(coma)
                # coma = sorted(coma)
                #? for removing empty strings and whitespaces
                cleaned_houses = [house.strip().lstrip('\r\n') for house in coma]
                coma = sorted(cleaned_houses, key=lambda x: int(''.join(filter(str.isdigit, x))))

                # while "" in coma:
                #     coma.remove("")   
                return coma
            elif obj.houses[0] == '[':
                return sorted(obj.houses[1:-1].split(', '))
               
            else: 
                space = obj.houses.split(' ')
                space = set(space)
                space = list(space)
                # space = sorted(space)
                #? for removing empty strings and whitespaces
                space = sorted(space, key=CoverageCitiesSerializer.extract_alphanumeric_parts)


                return space
        except:
            return []
        
    def get_city(self, obj):
        return obj.city

    class Meta:
        model = Coverages
        fields = [
            'city',
            'district',
            'street',
            'houses',
        ]


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    plans = serializers.SerializerMethodField()

    def get_plans(self, obj):
        has_none = False
        for i in obj.plans.all():
            if i.provider.is_published == False:
                has_none = True
                return None
        if not has_none:
            return [
                {
                    'plan_id': plan.id,
                    'provider_name': plan.provider.name,
                    'provider_picture': plan.provider.picture.url,
                    'provider_position': plan.provider.position,
                    'name': plan.name,
                    'title': plan.title,
                    'price': plan.price,
                    'tech': plan.tech,
                    'day': plan.day,
                    'night': plan.night,
                    'speed': plan.speed,
                    'limit': plan.limit,
                    'is_hot': plan.is_hot,
                    'router': plan.router,
                    'router_text': plan.router_text,
                    'tv': plan.tv,
                    'tv_text': plan.tv_text,
                    'cabel': plan.cabel,
                    'cabel_text': plan.cabel_text,
                    'more_info': plan.more_info,
                }
                for plan in obj.plans.all()
            ]

    class Meta:
        model = Offer
        fields = '__all__'


class TopProviderSerializer(serializers.ModelSerializer):
    provider_name = serializers.SerializerMethodField()
    provider_picture = serializers.SerializerMethodField()
    provider_is_published = serializers.SerializerMethodField()

    def get_provider_picture(self, obj):
        return obj.provider.picture.url

    def get_provider_name(self, obj):
        return obj.provider.name

    def get_provider_is_published(self, obj):
        return obj.provider.is_published

    class Meta:
        model = TopProviders
        fields = [
            'id',
            'provider_id',
            'provider_name',
            'provider_picture',
            'text',
            'provider_is_published'
        ]

    # def to_representation(self, instance):
    #     if instance.provider.is_published:
    #         return super().to_representation(instance)
    #     else:
    #         return None


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllProviders
        fields = [
            'id',
            'name',
            'picture',
            'info',
            # 'is_published',
        ]

    # def to_representation(self, provider):
    #     if provider.is_published:
    #         return super().to_representation(provider)
    #     else:
    #         return None


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = '__all__'


class AdresslessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adressless
        fields = [
            'id',
            'phone',
            'created',
        ]