# Generated by Django 3.2.6 on 2022-05-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_app', '0004_log_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
