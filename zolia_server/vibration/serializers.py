from rest_framework import serializers
from .models import VibrationSetting


class VibrationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VibrationSetting
        fields = "__all__"