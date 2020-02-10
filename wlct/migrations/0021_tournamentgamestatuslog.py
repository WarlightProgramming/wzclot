# Generated by Django 2.1.4 on 2019-05-23 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0020_tournamentgamelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentGameStatusLog',
            fields=[
                ('logger_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wlct.Logger')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wlct.TournamentGame')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wlct.Tournament')),
            ],
            bases=('wlct.logger',),
        ),
    ]