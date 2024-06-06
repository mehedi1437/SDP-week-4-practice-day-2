# Generated by Django 5.0.6 on 2024-06-04 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rating',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=2, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 5, 0, 25, 42, 473083)),
        ),
    ]
