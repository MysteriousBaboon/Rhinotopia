# Generated by Django 3.0.5 on 2020-05-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0021_auto_20200506_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='stat_Points',
            field=models.IntegerField(default=5),
        ),
    ]