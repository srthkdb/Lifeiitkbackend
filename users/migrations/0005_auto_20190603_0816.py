# Generated by Django 2.2.1 on 2019-06-03 08:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190602_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='earlier_login',
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='por',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True),
        ),
    ]
