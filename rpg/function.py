import random
from django.contrib.auth import login



def calculating_sucess(mission, character):
    result = (character.strength * mission.strength_Ratio) +\
             (character.intelligence * mission.intelligence_Ratio) +\
             (character.agility * mission.agility_Ratio)

    if random.randint(0, mission.success_Goal) <= result:
        levelup(character, mission.xp)
        character.save()
        return True
    else:
        return False


def evolve():

    #Change the experience needed for levelup
    pass


def levelup(character, xp):
    character.experience += xp
    while character.experience > character.experience_needed:
        character.level += 1
        character.experience -= character.experience_needed
        character.experience_needed = character.experience_needed + 10
        character.available_point += 5 #Change the value to add more point per level


def log_check(request):
    log_status = request.user.is_authenticated
    return log_status
