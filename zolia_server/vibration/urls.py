from django.urls import path
from .views import ListCreateVibrationSettingAPI, RetrieveVibrationSettingAPI

urlpatterns = [
    path("/", ListCreateVibrationSettingAPI.as_view()),
    path("/<str:name>", RetrieveVibrationSettingAPI.as_view()),
]