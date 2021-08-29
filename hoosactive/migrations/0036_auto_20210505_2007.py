# Generated by Django 3.1.5 on 2021-05-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosactive', '0035_merge_20210502_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningentry',
            name='entry_ptr',
        ),
        migrations.AddField(
            model_name='entry',
            name='extra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(choices=[['', 'State'], ['AL', 'AL'], ['AK', 'AK'], ['AZ', 'AZ'], ['AR', 'AR'], ['CA', 'CA'], ['CO', 'CO'], ['CT', 'CT'], ['DE', 'DE'], ['FL', 'FL'], ['GA', 'GA'], ['HI', 'HI'], ['ID', 'ID'], ['IL', 'IL'], ['IN', 'IN'], ['IA', 'IA'], ['KS', 'KS'], ['KY', 'KY'], ['LA', 'LA'], ['ME', 'ME'], ['MD', 'MD'], ['MA', 'MA'], ['MI', 'MI'], ['MN', 'MN'], ['MS', 'MS'], ['MO', 'MO'], ['MT', 'MT'], ['NE', 'NE'], ['NV', 'NV'], ['NH', 'NH'], ['NJ', 'NJ'], ['NM', 'NM'], ['NY', 'NY'], ['NC', 'NC'], ['ND', 'ND'], ['OH', 'OH'], ['OK', 'OK'], ['OR', 'OR'], ['PA', 'PA'], ['RI', 'RI'], ['SC', 'SC'], ['SD', 'SD'], ['TN', 'TN'], ['TX', 'TX'], ['UT', 'UT'], ['VT', 'VT'], ['VA', 'VA'], ['WA', 'WA'], ['WV', 'WV'], ['WI', 'WI'], ['WY', 'WY']], max_length=2),
        ),
        migrations.DeleteModel(
            name='PushUpsEntry',
        ),
        migrations.DeleteModel(
            name='RunningEntry',
        ),
    ]
