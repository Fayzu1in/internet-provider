from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from rest_framework import generics, viewsets
from rest_framework.response import Response 
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class PlansList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# ? TEST
class PlanViewsSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name','title','speed', 'price', 'provider']

    def get_queryset(self):
        name = self.request.query_params.get('name')
        title = self.request.query_params.get('title')
        provider = self.request.query_params.get('provider')
        if name:
            queryset = self.queryset.filter(name=name)
        elif title:
            queryset = self.queryset.filter(title=title)
        elif provider:
            queryset = self.queryset.filter(provider=provider)
        else:
            queryset = self.queryset
        return queryset
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class PlansDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# class CoverageList(generics.ListCreateAPIView):
#     queryset = Coverages.objects.all()
#     serializer_class = CoverageSerializer

    
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
        serializer = self.get_serializer(instance, data=request.data, partial=True)
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

# Create your views here.
def home(request):
    context = {}
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
