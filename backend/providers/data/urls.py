from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

# ? coverage
router.register("v1/coverage", views.CoverageViewSet)
# ? q&a
router.register(r"v1/q&a", views.QuestionAndAnswerView)

urlpatterns = [
    # ? plans
    path("v1/plans/<int:pk>", views.PlansDetail.as_view()),
    path("v1/plans/", views.PlansListAPIView.as_view()),
    # ? coverage
    path("v1/coverage-cities/", views.CoverageCityViewSet.as_view()),
    path("v1/coverage-check/", views.CoverageCheck.as_view()),
    path("v1/coverage/<int:pk>", views.CoverageDetail.as_view()),
    # ? callbacks
    path("v1/callbacks", views.CallbackList.as_view()),
    path("v1/noaddress-callback/", views.AdresslessListView.as_view()),
    path("v1/quick/", views.QuickCallbackList.as_view()),
    path(
        "v1/bot-callback/",
        views.BotCallbackCreate.as_view(),
        name="bot-callback_create",
    ),
    # path('v1/callbacks/<int:pk>', views.CallbackDetail.as_view()),
    # ? offers
    path("v1/offers", views.OfferList.as_view()),
    path("v1/offers/<int:pk>", views.OfferDetail.as_view()),
    # ? providers
    path("v1/providers", views.ProvidersList.as_view()),
    path("v1/providers/<int:pk>", views.ProvidersDetail.as_view()),
    path("v1/top-providers", views.TopProviderList.as_view()),
    path("v1/top-providers/<int:pk>", views.TopProviderDetail.as_view()),
    # ? bot users
    path("v1/bot-users", views.BotUsersList.as_view()),
    path("v1/bot-user/<int:pk>", views.BotUsersDetail.as_view()),
    # ? click events
    path("v1/click", views.ClieckEventView.as_view(), name="user_click"),
]

urlpatterns += router.urls

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
