from django.db import models


class VibrationSetting(models.Model):
    userID = models.ForeignKey(
        "account.User", on_delete=models.CASCADE
    )  # "hanbin8269@gmail.com"
    name = models.CharField(default="")  # "진동1"
    isAlarm = models.BooleanField(default=False)  # True
    alarmTimeTo = models.CharField(null=True)  # "08:00"
