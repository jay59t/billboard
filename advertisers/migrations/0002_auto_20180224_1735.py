# Generated by Django 2.0.2 on 2018-02-24 14:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('advertisers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True,
                                       default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
