# Generated by Django 3.1.4 on 2020-12-04 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VibrationSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('isAlarm', models.BooleanField(default=False)),
                ('alarmTimeTo', models.CharField(max_length=128, null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VibrationPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('sequence', models.IntegerField()),
                ('vibrationSettingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vibration.vibrationsetting')),
            ],
        ),
    ]