from django.db import models


class VibrationSetting(models.Model):
    userID = models.ForeignKey(
        "account.User", on_delete=models.CASCADE
    )  # "hanbin8269@gmail.com"
    name = models.CharField(default="", max_length=128)  # "진동1"
    isAlarm = models.BooleanField(default=False)  # True
    alarmTimeTo = models.CharField(null=True, max_length=128)  # "08:00"


class VibrationPattern(models.Model):
    vibrationSettingID = models.ForeignKey(VibrationSetting, on_delete=models.CASCADE)
    value = models.IntegerField()
    sequence = models.IntegerField()