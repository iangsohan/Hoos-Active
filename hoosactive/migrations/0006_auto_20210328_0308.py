# Generated by Django 3.1.7 on 2021-03-28 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosactive', '0005_auto_20210328_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 3, 8, 45, 2998)),
        ),
    ]
