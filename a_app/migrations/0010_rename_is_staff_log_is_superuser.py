# Generated by Django 3.2 on 2022-05-20 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_app', '0009_auto_20220518_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='is_staff',
            new_name='is_superuser',
        ),
    ]
