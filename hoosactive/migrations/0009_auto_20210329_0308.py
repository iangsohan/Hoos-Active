# Generated by Django 3.1.7 on 2021-03-29 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosactive', '0008_auto_20210328_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='cals_burned',
            new_name='calories',
        ),
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 3, 8, 14, 889574)),
        ),
    ]
