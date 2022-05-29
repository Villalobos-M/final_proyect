# Generated by Django 3.2 on 2022-05-27 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0006_alter_rack_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookitem',
            name='how',
        ),
        migrations.RemoveField(
            model_name='bookitem',
            name='user',
        ),
        migrations.AddField(
            model_name='bookitem',
            name='is_rent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='rack',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.rack'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='rent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('369b6183-b969-4885-99fd-e0309f0b261d')),
        ),
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('bb4acbed-f70b-4268-9e25-a6d5a6e4488f')),
        ),
    ]