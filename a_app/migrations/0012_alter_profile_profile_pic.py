# Generated by Django 3.2 on 2022-05-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_app', '0011_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
