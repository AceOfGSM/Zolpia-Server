from rest_framework import serializers
from .models import VibrationSetting, VibrationPattern


class VibrationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VibrationSetting
        fields = "__all__"


class VibrationPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = VibrationPattern
        fields = "__all__"