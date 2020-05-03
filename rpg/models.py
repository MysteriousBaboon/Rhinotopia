from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.DurationField()
    sucess = models.SmallIntegerField()
    isActive = models.BooleanField()

    #class Difficulty(models.TextChoices):

