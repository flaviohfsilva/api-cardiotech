from rest_framework import serializers
from pulse.models import Pulse

class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulse
        fields = '__all__'
