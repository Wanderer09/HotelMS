from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_type',
            name='room_rating',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
