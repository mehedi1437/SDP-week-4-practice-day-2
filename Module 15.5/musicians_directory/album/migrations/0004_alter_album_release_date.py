# Generated by Django 5.0.6 on 2024-06-05 02:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_album_musician_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 5, 8, 57, 23, 391638)),
        ),
    ]