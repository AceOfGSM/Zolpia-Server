from django.db import models


class SleepAnalysisResultManager(models.Manager):
    def partial_update(self, id, **validated_data):
        instance = self.get(id=id)

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        return instance


# Create your models here.
class SleepAnalysisResult(models.Model):

    objects = SleepAnalysisResultManager()

    userID = models.ForeignKey(
        "account.User", on_delete=models.CASCADE
    )  # hanbin8269@gmail.com
    sleepScore = models.FloatField(null=True)  # 87
    sleepTimeFrom = models.CharField(null=True, max_length=128)  # "22:00"
    sleepTimeTo = models.CharField(null=True, max_length=128)  # "7:00"
    deepSleepScore = models.IntegerField(null=True)  # 140
    shallowSleepScore = models.IntegerField(null=True)  # 130
    evalulation = models.CharField(null=True, max_length=256)  # "나쁘지 않게 주무셨네요 ㅋ"
    sleepDate = models.DateField()  # "2020-07-18"


class EEGData(models.Model):
    sleepAnalysisResultID = models.ForeignKey(
        SleepAnalysisResult, on_delete=models.CASCADE
    )  # 1
    statement = models.IntegerField()  # 1 : 수면 2 : 깊은 수면 3 : 얕은 수면 이런식으로
