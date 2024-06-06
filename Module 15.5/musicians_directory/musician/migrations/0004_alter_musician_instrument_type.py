# Generated by Django 5.0.6 on 2024-06-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0003_alter_musician_instrument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(choices=[('STRING', 'String'), ('WIND', 'Wind'), ('PERCUSSION', 'Percussion')], default=None, max_length=100),
        ),
    ]