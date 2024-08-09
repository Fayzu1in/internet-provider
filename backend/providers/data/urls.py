from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

# router.register('v1/plans', views.PlanViewsSet)
router.register("v1/coverage", views.CoverageViewSet)
router.register(r"v1/q&a", views.QuestionAndAnswerView)

# router.register('v1/bot-users', views.BotUsersList.as_view)

urlpatterns = [
    # path('', views.home, name='home'),
    # path('login', views.login_user, name='login'),
    # path('logout', views.logout_user, name='logout'),
    path("register", views.registration, name="register"),
    path("v1/plans/<int:pk>", views.PlansDetail.as_view()),
    path("v1/coverage/<int:pk>", views.CoverageDetail.as_view()),
    path("v1/callbacks", views.CallbackList.as_view()),
    # path('v1/callbacks/<int:pk>', views.CallbackDetail.as_view()),
    path("v1/offers", views.OfferList.as_view()),
    path("v1/offers/<int:pk>", views.OfferDetail.as_view()),
    path("v1/providers", views.ProvidersList.as_view()),
    path("v1/providers/<int:pk>", views.ProvidersDetail.as_view()),
    path("v1/top-providers", views.TopProviderList.as_view()),
    path("v1/top-providers/<int:pk>", views.TopProviderDetail.as_view()),
    # path('v1/news', views.NewsList.as_view()),
    # path('v1/news/<int:pk>', views.NewsDetail.as_view()),
    path("v1/bot-users", views.BotUsersList.as_view()),
    path("v1/bot-user/<int:pk>", views.BotUsersDetail.as_view()),
    path("v1/coverage-cities/", views.CoverageCityViewSet.as_view()),
    path("v1/coverage-check/", views.CoverageCheck.as_view()),
    path("v1/noaddress-callback/", views.AdresslessListView.as_view()),
    path("v1/plans/", views.PlansListAPIView.as_view()),
    path("v1/quick/", views.QuickCallbackList.as_view()),
    path("v1/click", views.ClieckEventView.as_view(), name="user_click"),
]

urlpatterns += router.urls

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
