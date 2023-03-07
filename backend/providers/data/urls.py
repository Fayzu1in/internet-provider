from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),
    path('plans', views.PlansList.as_view()),
    path('plans/<int:pk>/', views.PlansDetail.as_view()),
    path('coverage', views.CoverageList.as_view()),
    path('coverage/<int:pk>/', views.CoverageDetail.as_view()),
]
