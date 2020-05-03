import random


def calculating_sucess(chance):
    if random.randint(0,100) <= chance:
        return True
    else:
        return False
