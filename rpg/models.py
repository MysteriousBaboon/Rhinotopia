from django.db import models


# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name


class Character(models.Model):
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.character_name
