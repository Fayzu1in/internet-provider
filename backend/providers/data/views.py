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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


class PlansDetail(generics.RetrieveAPIView):
    queryset = Plan.objects.all().select_related("provider")
    # queryset = Plan.objects.filter(provider__is_published=True)
    serializer_class = PlanSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverages.objects.all()
    serializer_class = CoverageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["city", "district", "street", "house"]

    def get_queryset(self):
        city = self.request.query_params.get("city")
        street = self.request.query_params.get("street")
        district = self.request.query_params.get("district")
        house = self.request.query_params.get("house")
        queryset = self.queryset
        if city:
            queryset = queryset.filter(Q(city__icontains=city.capitalize()))
        if street:
            queryset = queryset.filter(Q(street=street))
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
        serializer = self.get_serializer(instance, data=request.data, partial=True)
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
        first_city = "Ташкент"
        second_city = "Ташкентская область"
        tashkent_cities = queryset.filter(city=first_city).order_by("city")
        tashkent_obl = queryset.filter(city=second_city).order_by("city")
        other_cities = queryset.exclude(city=first_city).order_by("city")
        queryset = list(tashkent_cities) + list(tashkent_obl) + list(other_cities)
        return queryset


@method_decorator(csrf_exempt, name="dispatch")
class CallbackList(generics.CreateAPIView):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer

    def post(self, request, *args, **kwargs):
        print("without csrf token")
        serializer = CallbackSerializer(data=request.data)
        if serializer.is_valid():
            callback = serializer.save()
            chosen_plan = get_object_or_404(Plan, id=request.data.get("plan_id"))

            response = f"""
Имя: <b>{callback.name}</b>
Номер телефона: <b>{callback.phone}</b>
Город: <b>{callback.city}</b>
Район: <b>{callback.district}</b>
Улица: <b>{callback.street}</b>
Дом: <b>{callback.house}</b>
Тариф: <b>{chosen_plan}</b>
Статус: <b>Opened</b>
Время: <b>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</b>

<i>UTM source: <b>{callback.utm_source }</b></i>
<i>UTM medium: <b>{callback.utm_medium }</b></i>
<i>UTM campaign: <b>{callback.utm_campaign}</b></i>
            """
            for i in admin_list:
                try:
                    bot.send_message(
                        i,
                        f"Новая заявка на обратный звонок от:\n\n{response}",
                        parse_mode="HTML",
                    )
                except Exception:
                    continue
            return Response(serializer.data)
        return Response(serializer.errors)

    # def get(self, request, *args, **kwargs):
    #     queryset = Callback.objects.all()

    #     if request.query_params.get('status'):
    #         queryset = queryset.filter(
    #             status=request.query_params.get('status'))

    #     return Response(queryset.values())


# class CallbackList(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = CallbackSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             chosen_plan = Plan.objects.get(id=request.data["plan_id"])
#             response = f"""
# Имя: <b>{request.data['name']}</b>
# Номер телефона: <b>{request.data['phone']}</b>
# Город: <b>{request.data['city']}</b>
# Район: <b>{request.data['district']}</b>
# Улица: <b>{request.data['street']}</b>
# Дом: <b>{request.data['house']}</b>
# Тариф: <b>{chosen_plan}</b>
# Статус: <b>Opened</b>
# Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>
#             """
#             for i in admin_list:
#                 bot.send_message(
#                     i,
#                     f"Новая заявка на обратный звонок от:\n\n{response}",
#                     parse_mode="HTML",
#                 )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         queryset = Callback.objects.all()

#         if request.query_params.get("status"):
#             queryset = queryset.filter(status=request.query_params.get("status"))

#         return Response(queryset.values(), status=status.HTTP_200_OK)


class CallbackDetail(generics.RetrieveAPIView):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer


class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all().prefetch_related("plans")
    serializer_class = OfferSerializer


class OfferDetail(generics.RetrieveAPIView):
    queryset = Offer.objects.all().prefetch_related("plans")
    serializer_class = OfferSerializer


class TopProviderList(generics.ListCreateAPIView):
    # queryset = TopProviders.objects.filter(provider__is_published=True)
    queryset = TopProviders.objects.filter().select_related("provider")
    serializer_class = TopProviderSerializer


class TopProviderDetail(generics.RetrieveAPIView):
    queryset = TopProviders.objects.all().select_related("provider")
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
    filter_fields = [
        "id",
        "name",
        "phone",
        "email",
        "address",
        "plan",
        "provider",
        "status",
    ]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        username = self.request.query_params.get("username")
        is_admin = self.request.query_params.get("email")
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
            callback = serializer.save()
            response = f"""
Номер телефона: <b>{callback.phone}</b>
Статус: <b>Opened</b>
Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>

<i>UTM source: <b>{callback.utm_source }</b></i>
<i>UTM medium: <b>{callback.utm_medium }</b></i>
<i>UTM campaign: <b>{callback.utm_campaign}</b></i>
            """
            for i in admin_list:
                try:
                    bot.send_message(
                        i, f"Новая заявка без адреса от:\n{response}", parse_mode="HTML"
                    )
                except Exception:
                    continue
            return Response(serializer.data)


def home(request):
    client_ip = request.META["REMOTE_ADDR"]
    providers = AllProviders.objects.all()
    context = {"client_ip": client_ip, "providers": providers}
    return render(request, "test.html", context=context)


def login_user(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context = {"form": UserForm, "error": "Incorrect password or username"}
            return render(request, "login.html", context)
    context = {"form": UserForm}

    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")


def registration(request):
    form = UserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("login")
    context = {"form": form}
    return render(request, "registration.html", context)


class CoverageCheck(APIView):
    PROVIDER_KEYS = [
        ("uzonline_houses", "Uztelecom"),
        ("sarkor_houses", "Sarkor Telecom"),
        ("comnet_houses", "Comnet"),
        ("freelink_houses", "Free Link"),
        ("ars_inform_houses", "Ars Inform"),
        ("city_net_houses", "City Net"),
        ("gals_houses", "Gals Telecom"),
        ("spectr_houses", "Spectr IT"),
        ("optikom_houses", "Optikom"),
        ("sirius_houses", "Sirius Telecom"),
        ("nano_houses", "Nano Telecom"),
    ]

    def get_provider_houses(self, required_address, provider_key):
        return required_address.get(provider_key, [])

    def get(self, request):
        city = request.query_params.get("city")
        street = request.query_params.get("street")
        house = str(request.query_params.get("house", "")).strip()
        district = request.query_params.get("district")

        # Fetch address data from external API
        required_address = None
        try:
            query = (
                f"?district={district}&street={street}"
                if district
                else f"?street={street}"
            )
            response = requests.get(f"http://internetbor.uz/api/v1/coverage/{query}")
            response.raise_for_status()
            required_address = response.json()[0]
            # print(required_address)
        except (requests.exceptions.RequestException, IndexError, KeyError):
            return Response(
                {"error": "Address not found or request failed"}, status=400
            )

        # Gather available providers based on house matching
        providers = ["Uztelecom"]  # Default provider
        for provider_key, provider_name in self.PROVIDER_KEYS:
            provider_houses = self.get_provider_houses(required_address, provider_key)
            if house in map(str.strip, map(str, provider_houses)):
                providers.append(provider_name)

        # print(providers)

        # Fetch provider and plans data
        found_providers = []
        if providers:
            provider_objs = AllProviders.objects.filter(
                name__in=providers
            ).prefetch_related("best_plans")
            print(provider_objs)
            for provider in provider_objs:
                plans = provider.best_plans.all()
                if not plans:
                    continue
                provider_data = {
                    "provider_id": provider.id,
                    "provider_name": provider.name,
                    "provider_picture": provider.picture.url,
                    "provider_info": provider.info,
                    "provider_position": provider.position,
                    "is_published": provider.is_published,
                    "provider_best": [
                        {
                            "plan_id": plan.id,
                            "plan_name": plan.title,
                            "plan_speed": plan.speed,
                            "plan_limit": plan.limit,
                            "plan_price": plan.price,
                            "plan_info": plan.info,
                            "provider_id": plan.provider.id,
                            "provider_name": plan.provider.name,
                            "provider_info": plan.provider.info,
                            "provider_picture": plan.provider.picture.url,
                            "tech": plan.tech,
                            "limit": plan.limit,
                            "day": plan.day,
                            "night": plan.night,
                            "info": plan.info,
                            "abonents": plan.abonents,
                            "is_hot": plan.is_hot,
                            "router": plan.router,
                        }
                        for plan in plans
                    ],
                }
                found_providers.append(provider_data)
        sorted_data = sorted(found_providers, key=lambda x: int(x["provider_position"]))
        return Response({"providers": sorted_data})


class PlansListAPIView(generics.ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.filter(provider__is_published=True).select_related(
        "provider"
    )

    def get(self, request, *args, **kwargs):
        provider = request.query_params.get("provider", None)
        if provider:
            plans = Plan.objects.filter(
                provider__id=provider, provider__is_published=True
            ).select_related("provider")
            serializer = PlanSerializer(plans, many=True)
            return Response(serializer.data)
        else:
            plans = Plan.objects.filter(provider__is_published=True).select_related(
                "provider"
            )
            serializer = PlanSerializer(plans, many=True)
            return Response(serializer.data)


class QuestionAndAnswerView(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionAndAnswers.objects.all()
    serializer_class = QuestionAndAnswerSerializer


class QuickCallbackList(generics.CreateAPIView):
    queryset = QuickCallback.objects.all()
    serializer_class = QuickCallbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = QuickCallbackSerializer(data=request.data)
        if serializer.is_valid():
            callback = serializer.save()
            # print(request.data)
            response = f"""
Имя: <b>{callback.name}</b>
Номер телефона: <b>{callback.phone}</b>
Удобное время: <b>{callback.preferrable_time}</b>
Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>

<i>UTM source: <b>{callback.utm_source }</b></i>
<i>UTM medium: <b>{callback.utm_medium }</b></i>
<i>UTM campaign: <b>{callback.utm_campaign}</b></i>
            """
            for i in admin_list:
                try:
                    bot.send_message(
                        i, f"Новая быстрая заявка:\n{response}", parse_mode="HTML"
                    )
                except Exception as e:
                    print(f"Error sending message to {i}: {e}")
                    continue
            return Response(serializer.data)
        return Response(serializer.errors)


@method_decorator(csrf_exempt, name="dispatch")
class ClieckEventView(APIView):
    def post(self, request, format=None):

        ip_address = request.META.get("REMOTE_ADDR")
        device = request.META.get("HTTP_USER_AGENT")

        try:
            title = request.data["title"]
        except KeyError:
            return Response(
                {"message": "title is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        data = {"ip": ip_address, "title": title, "device": device}

        serializer = ClickEventSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BotCallbackCreate(generics.CreateAPIView):
    queryset = BotCallback.objects.all()
    serializer_class = BotCallbackSerializer

    def post(self, request, format=None):
        serializer = BotCallbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = f"""
Имя: <b>{request.data['name']}</b>
Номер телефона: <b>{request.data['phone']}</b>
Адрес: <b>{request.data['address']}</b>
Время: <b>{datetime.today().strftime('%D %H:%M:%S')}</b>
"""
            for i in admin_list:
                try:
                    bot.send_message(
                        i,
                        f"Новая заявка с телеграм бота:\n{response}",
                        parse_mode="HTML",
                    )
                except Exception as e:
                    print(f"Error sending message to {i}: {e}")
                    continue
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
