from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .serializers import SleepAnalysisResultSerializer
from .models import SleepAnalysisResult


class ListCreateSleepAnalysisResultAPI(generics.ListCreateAPIView):
    queryset = SleepAnalysisResult.objects.all()
    serializer_class = SleepAnalysisResultSerializer
