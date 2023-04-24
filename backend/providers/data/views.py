from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from django.db.models import Q
from bot import bot, admin_list
from datetime import datetime
# from django.views.decorators.csrf import csrf_exempt
# from telegram import Update, Bot
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Dispatcher
# from telegram_bot.views import register_handlers
# import json
# from django.http import JsonResponse


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


class PlansDetail(generics.RetrieveUpdateDestroyAPIView):
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
                Q(street__icontains=street))
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


class CoverageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coverages.objects.all()
    serializer_class = CoverageSerializer


class CoverageCityViewSet(generics.ListCreateAPIView):
    queryset = Coverages.objects.all()
    serializer_class = CoverageCitiesSerializer


class CallbackList(generics.ListCreateAPIView):
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


class CallbackDetail(generics.RetrieveUpdateAPIView):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer


class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferDetail(generics.RetrieveUpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class TopProviderList(generics.ListCreateAPIView):
    # queryset = TopProviders.objects.filter(provider__is_published=True)
    queryset = TopProviders.objects.filter()
    serializer_class = TopProviderSerializer


class TopProviderDetail(generics.RetrieveUpdateAPIView):
    queryset = TopProviders.objects.all()
    serializer_class = TopProviderSerializer


class ProvidersList(generics.ListCreateAPIView):
    queryset = AllProviders.objects.filter(is_published=True)
    # queryset = AllProviders.objects.filter()
    serializer_class = ProviderSerializer


class ProvidersDetail(generics.RetrieveUpdateAPIView):
    queryset = AllProviders.objects.all()
    serializer_class = ProviderSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateAPIView):
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


class BotUsersDetail(generics.RetrieveUpdateAPIView):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer

# Create your views here.


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


# @csrf_exempt
# def telegram_webhook(request):
#     if request.method == "POST":
#         json_data = json.loads(request.body.decode("utf-8"))
#         update = Update.de_json(json_data, bot)
#         dispatcher.process_update(update)
#     return JsonResponse({"status": "ok"})

# # Initialize the Telegram bot and dispatcher
# bot = Bot(token="YOUR_BOT_TOKEN")
# dispatcher = Dispatcher(bot, None)
# register_handlers(dispatcher)
