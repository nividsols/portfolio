# Generated by Django 5.0.6 on 2024-07-13 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_remove_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='companies/'),
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_no', models.IntegerField()),
                ('title', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(blank=True, null=True)),
                ('case_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.casestudy')),
            ],
        ),
    ]
