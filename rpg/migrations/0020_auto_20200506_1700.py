# Generated by Django 3.0.5 on 2020-05-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0019_auto_20200506_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default='Unspecified', max_length=15),
        ),
        migrations.AddField(
            model_name='character',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Undefined', 'Undefined')], default='Undefined', max_length=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='specie',
            field=models.CharField(choices=[('Elf', 'Elf'), ('Orc', 'Ork'), ('Human', 'Human')], default='Human', max_length=10),
        ),
    ]
