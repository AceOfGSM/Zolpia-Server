from django.urls import path
from .views import (
    CreateSleepAnalysisResultAPI,
    UpdateSleepAnalysisResultAPI,
    RetrieveSleepAnalysisResultAPI,
)

urlpatterns = [
    path("/", CreateSleepAnalysisResultAPI.as_view()),
    path("/<int:sleepAnalysisResultID>/", RetrieveSleepAnalysisResultAPI.as_view()),
    path(
        "/sleep-end/<int:sleepAnalysisResultID>/",
        UpdateSleepAnalysisResultAPI.as_view(),
    ),
]