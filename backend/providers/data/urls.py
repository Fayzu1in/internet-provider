from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),
    path('api/v1/plans', views.PlansList.as_view()),
    path('api/v1/plans/<int:pk>/', views.PlansDetail.as_view()),
    path('api/v1/coverage', views.CoverageList.as_view()),
    path('api/v1/coverage/<int:pk>/', views.CoverageDetail.as_view()),
    path('api/v1/callbacks', views.CallbackList.as_view()),
    path('api/v1/calbacks/<int:pk>/', views.CallbackDetail.as_view()),
    path('api/v1/offers', views.OfferList.as_view()),
    path('api/v1/offers/<int:pk>/', views.OfferDetail.as_view()),
    path('api/v1/top-providers', views.TopProviderList.as_view()),
    path('api/v1/top-providers/<int:pk>/', views.TopProviderDetail.as_view()),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)