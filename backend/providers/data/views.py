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

class PlansList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanViewsSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
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
            queryset = self.queryset.filter(provider__name__contains=provider_name)
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
    serializer_class = PlanSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverages.objects.all()
    serializer_class = CoverageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['street', 'district']

    def get_queryset(self):
        street = self.request.query_params.get('street')
        district = self.request.query_params.get('district')
        if street:
            queryset = self.queryset.filter(street__contains=street)
        elif district:
            queryset = self.queryset.filter(district__contains=district)
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


class CoverageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coverages.objects.all()
    serializer_class = CoverageSerializer


class CallbackList(generics.ListCreateAPIView):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer


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
    queryset = TopProviders.objects.all()
    serializer_class = TopProviderSerializer


class TopProviderDetail(generics.RetrieveUpdateAPIView):
    queryset = TopProviders.objects.all()
    serializer_class = TopProviderSerializer


class ProvidersList(generics.ListCreateAPIView):
    queryset = AllProviders.objects.all()
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
    context = {'client_ip': client_ip}
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


