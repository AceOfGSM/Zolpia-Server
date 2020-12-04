from django.urls import path
from .views import ListCreateSleepAnalysisResultAPI, UpdateSleepAnalysisResultAPI

urlpatterns = [
    path("/", ListCreateSleepAnalysisResultAPI.as_view()),
    path("/sleep-end/<sleepAnalysisResultID>/", UpdateSleepAnalysisResultAPI.as_view()),
]