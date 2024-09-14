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

    class Meta:
        model = Subscription
        fields = ('id', 'name', 'tariff_id', 'client_name', 'email', 'tariff')
