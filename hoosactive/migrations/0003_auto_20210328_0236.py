# Generated by Django 3.1.7 on 2021-03-28 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosactive', '0002_auto_20210328_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 2, 36, 14, 727443)),
        ),
    ]
