from django.contrib import admin

from services.models import Service, Tariff, Subscription

admin.site.register(Service)
admin.site.register(Tariff)
admin.site.register(Subscription)
