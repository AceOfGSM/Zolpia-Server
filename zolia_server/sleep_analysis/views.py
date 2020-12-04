from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .serializers import SleepAnalysisResultSerializer
from .models import SleepAnalysisResult


class ListCreateSleepAnalysisResultAPI(generics.ListCreateAPIView):
    queryset = SleepAnalysisResult.objects.all()
    serializer_class = SleepAnalysisResultSerializer


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

        serialized = self.get_serializer(data=instance)
        serialized.update(instance, **data)
        serialized.is_valid()
        return Response(data={"message": "process complete"}, status=status.HTTP_200_OK)
