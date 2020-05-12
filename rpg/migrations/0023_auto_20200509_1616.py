# Generated by Django 3.0.5 on 2020-05-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0022_character_stat_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='xp',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='agility',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=0),
        ),
    ]
