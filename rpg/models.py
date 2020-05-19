from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character_number = models.IntegerField(default=0)
    character_number_max = models.IntegerField(default=3)
    missions_access = []


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Character(models.Model):
    # Owner
    owner_id = models.IntegerField(default=0)

    # Description and Name
    name = models.CharField(max_length=40)
    description = models.TextField()

    # Is available for mission
    isOccupied = models.BooleanField(default=False)

    # Experience and Level related
    experience = models.IntegerField(default=0)
    experience_needed = models.IntegerField(default=1)
    level = models.IntegerField(default=0)

    # Statistics
    available_point = models.IntegerField(default=5)

    strength = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)

    strength_final = models.IntegerField(default=1)
    intelligence_final = models.IntegerField(default=1)
    agility_final = models.IntegerField(default=1)

    # Species available
    class Species(models.TextChoices):
        ELF = 'Elf',
        ORK = 'Orc',
        HUMAN = 'Human',

    specie = models.CharField(max_length=10,
                              choices=Species.choices,
                              default=Species.HUMAN, )

    # Race of the character
    race = models.CharField(max_length=15, default='Unspecified')

    # Cosmetic
    class Sex(models.TextChoices):
        MALE = 'Male',
        FEMALE = 'Female',
        OTHER = 'Other',
        UNDEFINED = 'Undefined'

    sex = models.CharField(max_length=10,
                           choices=Sex.choices,
                           default=Sex.UNDEFINED)

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    isActive = models.BooleanField()
    duration = models.DurationField()

    success_Goal = models.IntegerField(default=1)
    strength_Ratio = models.FloatField(default=1)
    intelligence_Ratio = models.FloatField(default=1)
    agility_Ratio = models.FloatField(default=1)

    xp = models.IntegerField(default=1)

    def __str__(self):
        return self.name
