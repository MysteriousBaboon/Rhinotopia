from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=200)
    place_description = models.CharField(max_length=600)

    def __str__(self):
        return self.place_name


class Character(models.Model):
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.character_name
