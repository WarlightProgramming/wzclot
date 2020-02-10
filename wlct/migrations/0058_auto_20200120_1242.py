# Generated by Django 2.1.4 on 2020-01-20 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0057_realtimeladder_realtimeladdertemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentgame',
            name='game_start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 20, 12, 42, 26, 433683)),
        ),
        migrations.AddField(
            model_name='tournamentteam',
            name='joined_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]