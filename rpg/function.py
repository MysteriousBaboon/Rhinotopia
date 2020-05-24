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
        character.save()
        return False


def charactercheck(character):
    if character.isAlive:  # Check if the character is alive or respawn it after a cd
        if character.hp <= 0:
            character.isAlive = False
            character.respawnDate = datetime.now(timezone.utc) + timedelta(hours=2)
        elif character.hp < character.max_Hp and datetime.now(timezone.utc) > character.regenDate:
            character.hp += 2
            character.regenDate = datetime.now(timezone.utc) + timedelta(minutes=20)

    else:
        if character.respawnDate < datetime.now(timezone.utc):
            character.isAlive = True
            character.hp = character.max_Hp

    if character.level == 0:
        evolve(character)
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
        character.available_point += 5  # Change the value to add more point per level


def evolve(character):
    character.evolution_level += 1

    if character.specie == 'Spider':
        if character.evolution_level == 1:
            character.race = 'Little Spider'
        elif character.evolution_level == 2:
            character.race = 'Medium Spider'
        elif character.evolution_level == 3:
            character.race = 'Big Spider'
        elif character.evolution_level == 4:
            character.race = 'Gigantic Spider'

    elif character.specie == 'Insectoid':
        if character.evolution_level == 1:
            character.race = 'Little Scolopendre'
        elif character.evolution_level == 2:
            character.race = 'Medium Scolopendre'
        elif character.evolution_level == 3:
            character.race = 'Big Scolopendre'
        elif character.evolution_level == 4:
            character.race = 'Gigantic Scolopendre'

    elif character.specie == 'Rhinoceros':
        if character.evolution_level == 1:
            character.race = 'Little Rhinoceros'
        elif character.evolution_level == 2:
            character.race = 'Medium Rhinoceros'
        elif character.evolution_level == 3:
            character.race = 'Big Rhinoceros'
        elif character.evolution_level == 4:
            character.race = 'Gigantic Rhinoceros'

    elif character.specie == 'Canine':
        if character.evolution_level == 1:
            character.race = 'Little Canine'
        elif character.evolution_level == 2:
            character.race = 'Medium Canine'
        elif character.evolution_level == 3:
            character.race = 'Big Canine'
        elif character.evolution_level == 4:
            character.race = 'Gigantic Canine'

    elif character.specie == 'Feline':
        if character.evolution_level == 1:
            character.race = 'Little Feline'
        elif character.evolution_level == 2:
            character.race = 'Medium Feline'
        elif character.evolution_level == 3:
            character.race = 'Big Feline'
        elif character.evolution_level == 4:
            character.race = 'Gigantic Feline'

    elif character.specie == 'Ursidae':
        if character.evolution_level == 1:
            character.race = 'Little Ursidae'
        elif character.evolution_level == 2:
            character.race = 'Medium Ursidae'
        elif character.evolution_level == 3:
            character.race = 'Big Ursidae'
        elif character.evolution_level == 4:
            character.race = 'Gigantic Ursidae'

    character.can_Evolve = False
    character.save()


