# Generated by Django 3.0.6 on 2020-07-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_auto_20200725_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='housekeeping_status',
            field=models.CharField(default='room_cleaned', max_length=100),
        ),
    ]
