# Generated by Django 3.0.6 on 2020-05-22 05:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0044_auto_20200522_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 5, 12, 20, 203032, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='character',
            name='specie',
            field=models.CharField(choices=[('Spider', 'Spider'), ('Insectoid', 'Insectoid'), ('Rhinoceros', 'Rhinoceros'), ('Canine', 'Canine'), ('Feline', 'Feline'), ('Ursidae', 'Ursidae'), ('Human', 'Human')], default='Human', max_length=10),
        ),
    ]
