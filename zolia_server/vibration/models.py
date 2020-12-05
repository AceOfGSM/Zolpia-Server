from django.db import models


class VibrationSetting(models.Model):
    userID = models.ForeignKey(
        "account.User", on_delete=models.CASCADE
    )  # "hanbin8269@gmail.com"
    vibrationPatternName = models.ForeignKey(
        "vibration.VibrationPattern", on_delete=models.CASCADE, null=True
    )

    name = models.CharField(default="", max_length=128)  # "진동1"
    isAlarm = models.BooleanField(default=False)  # True
    alarmTimeTo = models.CharField(null=True, max_length=128)  # "08:00"


class VibrationPattern(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    pattern = models.CharField(max_length=256, default="")