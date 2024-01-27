from rest_framework import serializers
from everest_broker.models import ReceivedData

class LatestReceivedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedData
        fields = '__all__'
