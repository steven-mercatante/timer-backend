# Generated by Django 2.2.7 on 2019-11-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='starts',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='timer',
            name='stops',
            field=models.TextField(default='[]'),
        ),
    ]
