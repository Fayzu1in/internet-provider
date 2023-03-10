from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from rest_framework import generics
from .models import Plan, Coverage, Callback, Offer, TopProvider
from .serializers import PlanSerializer, CoverageSerializer, CallbackSerializer, OfferSerializer, TopProviderSerializer

class PlansList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlansDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class CoverageList(generics.ListCreateAPIView):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer

class CoverageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coverage.objects.all()
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
    queryset = TopProvider.objects.all()
    serializer_class = TopProviderSerializer


class TopProviderDetail(generics.RetrieveUpdateAPIView):
    queryset = TopProvider.objects.all()
    serializer_class = TopProviderSerializer


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
            context = {'form': UserForm, 'error': 'Incorrect password or username'}
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


