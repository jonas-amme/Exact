# Generated by Django 3.2.11 on 2023-01-09 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20230109_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ui_user',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ui', to=settings.AUTH_USER_MODEL),
        ),
    ]
