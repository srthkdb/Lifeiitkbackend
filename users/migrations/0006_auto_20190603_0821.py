# Generated by Django 2.2.1 on 2019-06-03 08:21

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190603_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='por',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
    ]
