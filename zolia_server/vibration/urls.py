from django.urls import path
from .views import (
    ListCreateVibrationSettingAPI,
    RetrieveVibrationSettingAPI,
    ListCreateVibrationPatternAPI,
)

urlpatterns = [
    path("/", ListCreateVibrationSettingAPI.as_view()),
    path("/<str:name>", RetrieveVibrationSettingAPI.as_view()),
    path("/vibration-patterns/", ListCreateVibrationPatternAPI.as_view()),
]