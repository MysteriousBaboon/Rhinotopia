# Generated by Django 3.0.6 on 2020-05-20 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0032_auto_20200520_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='finishtime',
        ),
    ]
