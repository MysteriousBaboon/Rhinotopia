import random
from datetime import datetime, timezone
from .models import Mission, Character


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


def mission_selection(request):
    mission_list = []
    if request.user.profile.missions_access:
        pass

    else:  # Choose which missions
        all_characters = Character.objects.filter(owner_id=request.user.id)

        for character in all_characters:
            mission_difficulty = character.level * random.random()
            if mission_difficulty < 1:
                rank = 'F'
            elif mission_difficulty < 2:
                rank = 'E'
            elif mission_difficulty < 4:
                rank = 'D'
            elif mission_difficulty < 7:
                rank = 'C'
            elif mission_difficulty < 10:
                rank = 'B'
            elif mission_difficulty < 15:
                rank = 'A'
            elif mission_difficulty < 18:
                rank = 'S'
            elif mission_difficulty < 20:
                rank = 'SSS'

            rand_mission = random.choice(Mission.objects.filter(difficulty=rank))# TODO add filter to don't have double
            mission_list.append(rand_mission)
        return mission_list


def sendmission(character, mission):
    character.isOccupied = True
    character.mission_id = mission.id
    mission.save()
    character.finishTime = datetime.now(timezone.utc) + mission.duration
    character.save()


def resultmission(character):
    mission = Mission.objects.get(id=character.mission_id)
    isSuccess = calculating_sucess(mission, character)
    character.isOccupied = False
    character.mission_id = 0
    character.save()
    return isSuccess


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