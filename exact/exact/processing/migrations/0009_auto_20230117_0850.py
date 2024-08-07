# Generated by Django 3.2.11 on 2023-01-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0008_auto_20230109_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pluginresultbitmap',
            name='transformation_matrix',
        ),
        migrations.AddField(
            model_name='pluginresultbitmap',
            name='frame',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pluginresultbitmap',
            name='location_rect',
            field=models.JSONField(default='{ "x": 0,"y": 0,"w": 10000,"h": 10000 }', null=True),
        ),
        migrations.AlterField(
            model_name='pluginresultbitmap',
            name='meta_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
