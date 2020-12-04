from django.urls import path
from .views import CreateVibrationSettingAPI

urlpatterns = [
    path("/", CreateVibrationSettingAPI.as_view()),
]