from django.db import models

# Create your models here.
class SleepAnalysisResult(models.Model):
    userID = models.ForeignKey("account.User")  # hanbin8269@gmail.com
    sleepScore = models.FloatField()  # 87
    sleepTimeFrom = models.CharField(null=True)  # "22:00"
    sleepTimeTo = models.CharField(null=True)  # "7:00"
    deepSleepTime = models.IntegerField(null=True)  # 140
    shallowSleepTime = models.IntegerField(null=True)  # 130
    evalulation = models.CharField(null=True)  # "나쁘지 않게 주무셨네요 ㅋ"
    sleepDate = models.DateField()  # "2020-07-18"


class EEGData(models.Model):
    sleepAnalysisResultID = models.ForeignKey(SleepAnalysisResult)  # 1
    statement = models.IntegerField()  # 1 : 수면 2 : 깊은 수면 3 : 얕은 수면 이런식으로
