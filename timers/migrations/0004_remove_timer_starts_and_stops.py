# Generated by Django 2.2.7 on 2019-11-24 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timers', '0003_timerstart_timerstop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='starts',
        ),
        migrations.RemoveField(
            model_name='timer',
            name='stops',
        ),
    ]
