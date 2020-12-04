from django.urls import path
from .views import CreateVibrationSettingAPI, RetrieveVibrationSettingAPI

urlpatterns = [
    path("/", CreateVibrationSettingAPI.as_view()),
    path("/<str:name>", RetrieveVibrationSettingAPI.as_view()),
]