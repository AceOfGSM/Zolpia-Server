from django.urls import path
from .views import SleepAnalysisResultListCreateAPI

urlpatterns = [
    path("/", SleepAnalysisResultListCreateAPI.as_view()),
]