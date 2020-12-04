from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .serializers import SleepAnalysisResultSerializer
from .models import SleepAnalysisResult, EEGData


class CreateSleepAnalysisResultAPI(generics.CreateAPIView):
    queryset = SleepAnalysisResult.objects.all()
    serializer_class = SleepAnalysisResultSerializer


class RetrieveSleepAnalysisResultAPI(generics.RetrieveAPIView):
    queryset = SleepAnalysisResult.objects.all()
    serializer_class = SleepAnalysisResultSerializer

    def get(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["sleepAnalysisResultID"])
        serializer = self.get_serializer(instance)

        result = serializer.data

        result["EEGData"] = [
            eegData["statement"]
            for eegData in EEGData.objects.filter(
                sleepAnalysisResultID=kwargs["sleepAnalysisResultID"]
            ).values("statement")
        ]

        return Response(data=result, status=status.HTTP_200_OK)


class UpdateSleepAnalysisResultAPI(generics.UpdateAPIView):
    queryset = SleepAnalysisResult.objects.all()
    serializer_class = SleepAnalysisResultSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["sleepAnalysisResultID"])

        data = {
            "sleepScore": 23,
            "sleepTimeFrom": "00:00",
            "sleepTimeTo": "06:00",
            "deepSleepScore": 170,
            "shallowSleepScore": 200,
            "evalulation": "못잤네 조금?",
        }
        # data = {
        #    "sleepScore" : sleepScore 구해주는 함수,
        #    "sleepTimeFrom" : sleepTimeFrom 구해주는 함수
        #    "sleepTimeTo" : sleepTimeTo 구해주는 함수
        #    "deepSleepTime" : deepSleepTime 구해주는 함수
        #    "shallowSleepTime" : shallowSleepTime 구해주는 함수
        #    "evalulation" : evalulation 구해주는 함수
        # }

        serializer = self.get_serializer(data=instance)
        serializer.update(instance, **data)
        serializer.is_valid()
        return Response(data={"message": "process complete"}, status=status.HTTP_200_OK)
