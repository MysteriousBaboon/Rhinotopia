# Generated by Django 3.0.5 on 2020-05-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0009_character_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='isOccupied',
            field=models.BooleanField(null=True),
        ),
    ]
