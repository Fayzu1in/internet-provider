from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),
    path('api/v1/plans', views.PlansList.as_view()),
    path('api/v1/plans/<int:pk>/', views.PlansDetail.as_view()),
    path('api/v1/coverage', views.CoverageList.as_view()),
    path('api/v1/coverage/<int:pk>/', views.CoverageDetail.as_view()),
    path('api/v1/callbacks/', views.CallbackList.as_view()),
    path('api/v1/calbacks/<int:pk>/', views.CallbackDetail.as_view()),
]
