# Generated by Django 3.2 on 2022-05-23 22:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e509006f-2183-4ef0-bdbc-a75967eeb760')),
        ),
    ]