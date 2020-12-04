from rest_framework import serializers
from .models import SleepAnalysisResult


class SleepAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAnalysisResult
        fields = "__all__"

    def create(self, validated_data):
        ModelClass = self.Meta.model
        return ModelClass._default_manager.create(
            userID=validated_data["userID"], sleepDate=validated_data["sleepDate"]
        )

    def update(self, instance, **validated_data):
        ModelClass = self.Meta.model

        return ModelClass.objects.partial_update(id=instance.id, **validated_data)
