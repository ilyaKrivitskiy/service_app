from django.urls import path, include
from rest_framework import routers
from .views import SubscriptionView

service_router = routers.DefaultRouter(trailing_slash=False)
service_router.register('subscriptions', SubscriptionView, basename="subscriptions")

urlpatterns = [
    path('', include(service_router.urls)),
]
