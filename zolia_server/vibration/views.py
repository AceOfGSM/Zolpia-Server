from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import VibrationSetting, VibrationPattern
from .serializers import VibrationSettingSerializer, VibrationPatternSerializer


class ListCreateVibrationSettingAPI(generics.ListCreateAPIView):
    queryset = VibrationSetting.objects.all()
    serializer_class = VibrationSettingSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(userID=request.user.email)

        serializer = VibrationSettingSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        instance = self.queryset.filter(
            userID=request.data["userID"], name=request.data["name"]
        )

        if instance:  # userID 당 name은 중복 불가
            raise ValidationError(detail={"message": "same name already exists"})

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(detail={"message": "invalid data"})
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RetrieveVibrationSettingAPI(generics.RetrieveAPIView):
    queryset = VibrationSetting.objects.all()
    serializer_class = VibrationSettingSerializer

    def get(self, request, *args, **kwargs):
        instance = self.queryset.get(name=kwargs["name"], userID=request.user.email)

        serializer = self.get_serializer(instance)

        return Response(data=serializer.data, status=status.HTTP_200_OK)