# Generated by Django 3.1.5 on 2021-04-11 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hoosactive', '0012_auto_20210411_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_log',
        ),
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 43, 15, 108550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 8, 43, 15, 108932, tzinfo=utc)),
        ),
    ]
