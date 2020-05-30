import random
from datetime import datetime, timezone, timedelta
from .models import Mission, Character



def log_check(request):  # Check if the user is logged in
    log_status = request.user.is_authenticated
    return log_status


def mission_selection(request):  # Choose what mission to display based on the level of every character
    mission_list = []
    if request.user.profile.missions_access:
        pass

    else:
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
            else:
                rank = 'SSS'

            rand_mission = random.choice(Mission.objects.filter(difficulty=rank))
            while rand_mission in mission_list:
                rand_mission = random.choice(Mission.objects.filter(difficulty=rank))

            mission_list.append(rand_mission)
        return mission_list


def sendmission(character, mission):  # Send the character on mission
    character.isOccupied = True
    character.mission_id = mission.id
    mission.save()
    character.finishTime = datetime.now(timezone.utc) + mission.duration
    character.save()


def resultmission(character):  # Welcome back the character
    mission = Mission.objects.get(id=character.mission_id)
    isSuccess = calculating_sucess(mission, character)
    character.isOccupied = False
    character.mission_id = 0
    character.save()
    return isSuccess


def calculating_sucess(mission, character):  # Check if the mission is winned or failed
    result = (character.strength * mission.strength_Ratio) +\
             (character.intelligence * mission.intelligence_Ratio) +\
             (character.agility * mission.agility_Ratio)

    if random.randint(0, mission.success_Goal) <= result:
        levelup(character, mission.xp)
        character.save()
        return True
    else:
        character.hp -= mission.damage
        character.regenDate = datetime.now(timezone.utc)

        character.save()
        return False


def charactercheck(character):
    if character.isAlive:  # Check if the character is alive or respawn it after a cd
        minute_elapsed = (datetime.now(timezone.utc) - character.regenDate).seconds / 60
        if character.hp <= 0:
            character.isAlive = False
            character.respawnDate = datetime.now(timezone.utc) + timedelta(hours=2)
        while character.hp < character.max_Hp and minute_elapsed >= 30:
            character.hp += 1
            minute_elapsed -= 30
        if character.hp == character.max_Hp:
            character.regenDate = datetime.now(timezone.utc)

    else:
        if character.respawnDate < datetime.now(timezone.utc):
            character.isAlive = True
            character.hp = character.max_Hp

    if (character.level / 5) >= (1 * character.evolution_level):
        character.can_Evolve = True

    character.max_Hp = 1 + character.stamina * 2
    character.save()
    if character.mission_id != 0:
        return Mission.objects.get(id=character.mission_id)


def levelup(character, xp):  # Check if the character has enough xp and if it does, level up
    character.experience += xp
    while character.experience > character.experience_needed:
        character.level += 1
        character.experience -= character.experience_needed
        character.experience_needed = character.experience_needed + 10
        character.available_point += 3  # Change the value to add more point per level


def evolve(character):
    character.evolution_level += 1

    if character.specie == 'Spider':
        if character.evolution_level == 1:
            character.race = 'Patu Diga'
            character.agility += 2
            character.intelligence += 1

        elif character.evolution_level == 2:
            character.race = 'Ricinulei'
            character.strength += 1
            character.agility += 2
            character.stamina += 2
            character.intelligence += 1

        elif character.evolution_level == 3:
            character.race = 'Solifugae'
            character.agility += 3
            character.intelligence += 2
            character.strength += 2
            character.stamina += 3

        elif character.evolution_level == 4:
            character.race = 'Goliath'
            character.agility += 6
            character.intelligence += 5
            character.strength += 4
            character.stamina += 4

    elif character.specie == 'Insectoid':
        if character.evolution_level == 1:
            character.race = 'Scolopendra cingulata'
            character.agility += 2
            character.stamina += 1

        elif character.evolution_level == 2:
            character.race = 'Scolopendra'
            character.agility += 2
            character.strength += 2
            character.stamina += 2

        elif character.evolution_level == 3:
            character.race = 'Scolopendra Gigantea'
            character.agility += 3
            character.intelligence += 2
            character.strength += 3
            character.stamina += 2

        elif character.evolution_level == 4:
            character.race = 'Arthropluera'
            character.agility += 6
            character.intelligence += 4
            character.strength += 4
            character.stamina += 6

    elif character.specie == 'Rhinoceros':
        if character.evolution_level == 1:
            character.race = 'Menoceras'
            character.stamina += 2
            character.strength += 1

        elif character.evolution_level == 2:
            character.race = 'Diceratherium'
            character.stamina += 2
            character.strength += 2
            character.agility += 1
            character.intelligence += 1

        elif character.evolution_level == 3:
            character.race = 'Chalicotheno'
            character.stamina += 3
            character.strength += 3
            character.agility += 2
            character.intelligence += 2

        elif character.evolution_level == 4:
            character.race = 'Mastodonterino'
            character.stamina += 6
            character.strength += 6
            character.agility += 4
            character.intelligence += 4

    elif character.specie == 'Canine':
        if character.evolution_level == 1:
            character.race = 'Fox'
            character.strength += 1
            character.agility += 1
            character.stamina += 1

        elif character.evolution_level == 2:
            character.race = 'Jackal'
            character.stamina += 2
            character.strength += 2
            character.agility += 2

        elif character.evolution_level == 3:
            character.race = 'Maned Wolf'
            character.stamina += 2
            character.strength += 3
            character.agility += 3
            character.intelligence += 2

        elif character.evolution_level == 4:
            character.race = 'Canis Dirus'
            character.stamina += 4
            character.intelligence += 4
            character.agility += 6
            character.strength += 6

    elif character.specie == 'Feline':
        if character.evolution_level == 1:
            character.race = 'Prionailurus Rubiginosus'
            character.strength += 1
            character.agility += 2

        elif character.evolution_level == 2:
            character.race = 'Lynx'
            character.strength += 3
            character.agility += 3

        elif character.evolution_level == 3:
            character.race = 'Panthera Pardus'
            character.strength += 2
            character.agility += 3
            character.intelligence += 3
            character.stamina += 2

        elif character.evolution_level == 4:
            character.race = 'Panthera Tigris Altaica'
            character.strength += 5
            character.agility += 6
            character.intelligence += 5
            character.stamina += 3

    elif character.specie == 'Ursidae':
        if character.evolution_level == 1:
            character.race = 'Spectacled'
            character.stamina += 1
            character.strength += 2

        elif character.evolution_level == 2:
            character.race = 'Sloth'
            character.stamina += 2
            character.strength += 2
            character.intelligence += 1
            character.agility += 1

        elif character.evolution_level == 3:
            character.race = 'Giant'
            character.stamina += 3
            character.strength += 3
            character.intelligence += 2
            character.agility += 2

        elif character.evolution_level == 4:
            character.race = 'Kodiak'
            character.stamina += 6
            character.strength += 6
            character.intelligence += 4
            character.agility += 4

    character.can_Evolve = False
    character.save()


