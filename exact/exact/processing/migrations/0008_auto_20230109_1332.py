# Generated by Django 3.2.11 on 2023-01-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0007_pluginjob_attached_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pluginjob',
            name='attached_worker',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pluginjob',
            name='error_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pluginjob',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]