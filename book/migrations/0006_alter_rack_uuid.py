# Generated by Django 3.2 on 2022-05-25 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('09d74b06-46ef-4957-b6a8-a34c5c27c8ca')),
        ),
    ]
