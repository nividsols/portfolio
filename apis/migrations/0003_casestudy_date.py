# Generated by Django 5.0.6 on 2024-07-12 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_casestudy_image_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 7, 12, 18, 26, 57, 527556), null=True),
        ),
    ]
