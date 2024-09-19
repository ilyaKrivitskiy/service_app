from rest_framework import serializers

from services.models import Subscription, Tariff


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    tariff = TariffSerializer()
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.EmailField(source='client.user.email')
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return instance.service.full_price * (1 - instance.tariff.discount_percent / 100)

    class Meta:
        model = Subscription
        fields = ('id', 'name', 'tariff_id', 'client_name', 'email', 'tariff', 'price')
