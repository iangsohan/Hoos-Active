# Generated by Django 3.1.5 on 2021-04-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosactive', '0031_auto_20210421_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='receive_notifications',
            field=models.BooleanField(default=True),
        ),
    ]
