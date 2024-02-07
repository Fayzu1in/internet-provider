from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from django.db.models import Q
from bot import bot, admin_list
from datetime import datetime
import requests
import rest_framework
# from django.views.decorators.csrf import csrf_exempt
# from telegram import Update, Bot
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Dispatcher
# from telegram_bot.views import register_handlers
# import json
# from django.http import JsonResponse
# rest_framework.permissions.IsAdminUser


class PlansList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanViewsSet(viewsets.ModelViewSet):
    # queryset = Plan.objects.all()
    queryset = Plan.objects.filter(provider__is_published=True)
    serializer_class = PlanSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'title', 'speed', 'price', 'provider_name']

    def get_queryset(self):
        name = self.request.query_params.get('name')
        title = self.request.query_params.get('title')
        provider = self.request.query_params.get('provider')
        provider_name = self.request.query_params.get('provider_name')
        is_hot = self.request.query_params.get('is_hot')

        if name:
            queryset = self.queryset.filter(name=name)
        elif title:
            queryset = self.queryset.filter(title=title)
        elif provider:
            queryset = self.queryset.filter(provider=provider)
        elif provider_name:
            queryset = self.queryset.filter(
                provider__name__contains=provider_name)
        elif is_hot:
            queryset = self.queryset.filter(is_hot=is_hot)
        else:
            queryset = self.queryset
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# class PlansDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Plan.objects.all()
#     # queryset = Plan.objects.filter(provider__is_published=True)
#     serializer_class = PlanSerializer


class PlansDetail(generics.RetrieveAPIView):
    # permission_classes = [rest_framework.permissions.IsAdminUser]
    queryset = Plan.objects.all()
    # queryset = Plan.objects.filter(provider__is_published=True)
    serializer_class = PlanSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverages.objects.all()
    serializer_class = CoverageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city', 'district', 'street', 'house']

    def get_queryset(self):
        city = self.request.query_params.get('city')
        street = self.request.query_params.get('street')
        district = self.request.query_params.get('district')
        house = self.request.query_params.get('house')
        queryset = self.queryset
        if city:
            queryset = queryset.filter(Q(city__icontains=city.capitalize()))
        if street:
            queryset = queryset.filter(
                Q(street=street))
        if district:
            queryset = queryset.filter(Q(district__icontains=district))
        if house:
            for i in queryset:
                try:
                    if str(house) in i.houses:
                        return queryset
                    elif int(house) in i.houses:
                        return queryset
                    else:
                        return None
                except ValueError:
                    return None
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class CoverageDetail(generics.RetrieveAPIView):
    queryset = Coverages.objects.all()
    serializer_class = CoverageSerializer


class CoverageCityViewSet(generics.ListCreateAPIView):
    queryset = Coverages.objects.all()
    serializer_class = CoverageCitiesSerializer

    def get_queryset(self):
        queryset = Coverages.objects.all()
        first_city = 'Ташкент'
        second_city = 'Ташкентская область'
        tashkent_cities = queryset.filter(city=first_city).order_by('city')
        tashkent_obl = queryset.filter(city=second_city).order_by('city')
        other_cities = queryset.exclude(city=first_city).order_by('city')
        queryset = list(tashkent_cities) + \
            list(tashkent_obl) + list(other_cities)
        return queryset


class CallbackList(generics.CreateAPIView):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = CallbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            chosen_plan = Plan.objects.get(id=request.data['plan_id'])
            response = f'''
Имя: <b>{request.data['name']}</b>
Номер телефона: <b>{request.data['phone']}</b>
Город: <b>{request.data['city']}</b>
Район: <b>{request.data['district']}</b>
Улица: <b>{request.data['street']}</b>
Дом: <b>{request.data['house']}</b>
Тариф: <b>{chosen_plan}</b>
Статус: <b>Opened</b>
Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>
            '''
            for i in admin_list:
                bot.send_message(
                    i, f"Новая заявка на обратный звонок от:\n\n{response}", parse_mode='HTML')
            return Response(serializer.data)
        return Response(serializer.errors)

    # def get(self, request, *args, **kwargs):
    #     queryset = Callback.objects.all()

    #     if request.query_params.get('status'):
    #         queryset = queryset.filter(
    #             status=request.query_params.get('status'))

    #     return Response(queryset.values())


class CallbackDetail(generics.RetrieveAPIView):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer


class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferDetail(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class TopProviderList(generics.ListCreateAPIView):
    # queryset = TopProviders.objects.filter(provider__is_published=True)
    queryset = TopProviders.objects.filter()
    serializer_class = TopProviderSerializer


class TopProviderDetail(generics.RetrieveAPIView):
    queryset = TopProviders.objects.all()
    serializer_class = TopProviderSerializer


class ProvidersList(generics.ListCreateAPIView):
    queryset = AllProviders.objects.filter(is_published=True)
    # queryset = AllProviders.objects.filter()
    serializer_class = ProviderSerializer


class ProvidersDetail(generics.RetrieveAPIView):
    queryset = AllProviders.objects.all()
    serializer_class = ProviderSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class BotUsersList(generics.ListCreateAPIView):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer


class BotUsersViewSet(viewsets.ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'phone', 'email',
                     'address', 'plan', 'provider', 'status']

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        username = self.request.query_params.get('username')
        is_admin = self.request.query_params.get('email')
        if user_id:
            queryset = self.queryset.filter(user_id=user_id)
        elif username:
            queryset = self.queryset.filter(username=username)
        elif is_admin:
            queryset = self.queryset.filter(is_admin=is_admin)
        return queryset


class BotUsersDetail(generics.RetrieveAPIView):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer

# Create your views here.


class AdresslessListView(generics.ListCreateAPIView):
    queryset = Adressless.objects.all()
    serializer_class = AdresslessSerializer
    # admin_list = []
    # bot_users = requests.get('https://internetbor.uz/api/v1/bot-users').json()
    # for i in bot_users:
    #     if i['is_admin']:
    #         admin_list.append(i['user_id'])

    def post(self, request, *args, **kwargs):
        serializer = AdresslessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = f'''
Номер телефона: <b>{request.data['phone']}</b>
Статус: <b>Opened</b>
Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>
            '''
            for i in admin_list:
                bot.send_message(
                    i, f"Новая заявка без адреса от:\n{response}", parse_mode='HTML')
            return Response(serializer.data)


def home(request):
    client_ip = request.META['REMOTE_ADDR']
    providers = AllProviders.objects.all()
    context = {'client_ip': client_ip, 'providers': providers}
    return render(request, 'test.html', context=context)


def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'form': UserForm,
                       'error': 'Incorrect password or username'}
            return render(request, 'login.html', context)
    context = {'form': UserForm}

    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def registration(request):
    form = UserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration.html', context)


class CoverageCheck(APIView):

    def get(self, request):
        city = request.query_params.get('city', None)
        street = request.query_params.get('street', None)
        house = str(request.query_params.get('house', None))
        district = request.query_params.get('district', None)

        try:
            # required_adress = requests.get(f'http://127.0.0.1:8000/api/v1/coverage/?street={street}&house={house}').json()[0]
            # required_adress = requests.get(f'http://internetbor.uz/api/v1/coverage/?street={street}').json()[0]
            if district:
                required_adress = requests.get(
                    f'http://internetbor.uz/api/v1/coverage/?district={district}&street={street}').json()[0]
            else:
                required_adress = requests.get(
                    f'http://internetbor.uz/api/v1/coverage/?street={street}').json()[0]
        except:
            required_adress = None

        print(required_adress)

        try:
            uzonline_houses = required_adress['uzonline_houses']
        except:
            uzonline_houses = []


        try:
            sarkor_houses = required_adress['sarkor_houses']
        except:
            sarkor_houses = []
        try:

            comnet_houses = required_adress['comnet_houses']
        except:
            comnet_houses = []
        try:
            freelink_houses = required_adress['freelink_houses']
        except:
            freelink_houses = []

        try:
            ars_inform_houses = required_adress['ars_inform_houses']
        except:
            ars_inform_houses = []
        try:
            city_net_houses = required_adress['city_net_houses']
        except:
            city_net_houses = []
        try:
            gals_houses = required_adress['gals_houses']
        except:
            gals_houses = []

        try:
            spectr_houses = required_adress['spectr_houses']
        except:
            spectr_houses = []

        try:
            optikom_houses = required_adress['optikom_houses']
        except:
            optikom_houses = []

        try:
            sirius_houses = required_adress['sirius_houses']
        except:
            sirius_houses = []

        providers = []

        providers.append('Uztelecom')

        for i in sarkor_houses:
            if house.strip() == str(i).strip():
                providers.append("Sarkor Telecom")

        for i in comnet_houses:
            if house.strip() == str(i).strip():
                providers.append('Comnet')

        for i in freelink_houses:
            if house.strip() == str(i).strip():
                providers.append('Free Link')


        for i in ars_inform_houses:
            if house.strip() == str(i).strip():
                providers.append('Ars Inform')

        for i in city_net_houses:
            if house.strip() == str(i).strip():
                providers.append('City Net')

        for i in gals_houses:
            if house.strip() == str(i).strip():
                providers.append('Gals Telecom')

        for i in spectr_houses:
            if house.strip() == str(i).strip():
                providers.append('Spectr IT')

        for i in optikom_houses:
            if house.strip() == str(i).strip():
                providers.append('Optikom')

        for i in sirius_houses:
            if house.strip() == str(i).strip():
                providers.append('Sirius Telecom')

        found_providers = []
        if providers:
            for provider in providers:
                provider = AllProviders.objects.get(name=provider)
                provider_data = {
                    "provider_id": provider.id,
                    "provider_name": provider.name,
                    "provider_picture": provider.picture.url,
                    "provider_info": provider.info,
                    'provider_position': provider.position,
                    "is_published": provider.is_published,
                    "provider_best": [],
                }
                for plan in provider.best_plans.all():
                    provider_data['provider_best'].append(
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
                            'tech': plan.tech,
                            'limit': plan.limit,
                            'day': plan.day,
                            'night': plan.night,
                            'info': plan.info,
                            'abonents': plan.abonents,
                            'is_hot': plan.is_hot,
                            'router': plan.router
                        })
                found_providers.append(provider_data)
                sorted_data = sorted(
                    found_providers, key=lambda x: int(x['provider_position']))
            data = {
                "providers": sorted_data,
            }
        else:
            provider = AllProviders.objects.filter(name='Uztelecom').only('name').first()
            provider_data = {
                    "provider_id": provider.id,
                    "provider_name": provider.name,
                    "provider_picture": provider.picture.url,
                    "provider_info": provider.info,
                    'provider_position': provider.position,
                    "is_published": provider.is_published,
                    "provider_best": [],
                }
            for plan in provider.best_plans.all():
                    provider_data['provider_best'].append(
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
            found_providers.append(provider_data)
            sorted_data = sorted(
                found_providers, key=lambda x: int(x['provider_position']))

            data = {
                "providers": sorted_data,
            }

        return Response(data)


class PlansListAPIView(generics.ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.filter(provider__is_published=True)

    def get(self, request, *args, **kwargs):
        provider = request.query_params.get('provider', None)
        if provider:
            plans = Plan.objects.filter(provider__id=provider)
            serializer = PlanSerializer(plans, many=True)
            return Response(serializer.data)
        else:
            plans = Plan.objects.filter(provider__is_published=True)
            serializer = PlanSerializer(plans, many=True)
            return Response(serializer.data)


class QuestionAndAnswerView(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionAndAnswers.objects.all()
    serializer_class = QuestionAndAnswerSerializer


class QuickCallbackList(generics.ListCreateAPIView):
    queryset = QuickCallback.objects.all()
    serializer_class = QuickCallbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = QuickCallbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            response = f'''
Имя: <b>{request.data['name']}</b>
Номер телефона: <b>{request.data['phone']}</b>
Удобное время: <b>{request.data['preferrable_time']}</b>
Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>
            '''
            for i in admin_list:
                bot.send_message(
                    i, f"Новая быстрая заявка:\n{response}", parse_mode='HTML')
            return Response(serializer.data)
        return Response(serializer.errors)


class ClieckEventView(APIView):
    def post(self, request, format=None):

        ip_address = request.META.get('REMOTE_ADDR', '')
        device = request.META.get('HTTP_USER_AGENT')
        title = request.data['title']
        
        data = {
            'ip': ip_address,
            'title': title,
            'device': device
        }
        
        serializer = ClickEventSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
