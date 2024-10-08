from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.IntegerField()

    def __str__(self):
        return f"Service: {self.name}"


class Tariff(models.Model):
    name = models.CharField(max_length=50)
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=20)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return f"Tariff: {self.name}"


class Subscription(models.Model):
    name = models.CharField(max_length=50, default="sub_name")
    client = models.ForeignKey(Client, related_name="subscription", on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name="subscription", on_delete=models.PROTECT)
    tariff = models.ForeignKey(Tariff, related_name="subscription", on_delete=models.PROTECT)

    def __str__(self):
        return f"Subscription: {self.name}"
