# Generated by Django 3.0.6 on 2020-05-20 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0035_auto_20200520_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 23, 58, 16, 506019)),
        ),
    ]
