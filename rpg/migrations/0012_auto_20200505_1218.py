# Generated by Django 3.0.5 on 2020-05-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0011_auto_20200505_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='isOccupied',
            field=models.BooleanField(default=False),
        ),
    ]
