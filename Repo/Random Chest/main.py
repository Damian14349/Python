# gra w której masz 5 ruchów w jedną stronę poprzez komnatę. Za każdym razem masz szansę wylosować skrzynkę lub nic

import random
from enum import Enum


def movement():
    move = 0
    while move < 5:
        input("Press any key to move!")
        chest_or_nothing()
        move = move + 1
        # chest_or_nothing()


def chest_or_nothing():
    event = ["Chest", "Nothing"]
    rng = random.choices(event, [60, 40])
    if rng == ["Nothing"]:
        print("You found nothing, move on!")
    elif rng == ["Chest"]:
        chests_types = ["green_chest", "orange_chest", "purple_chest", "gold_chest"]
        green_chest = 1000
        orange_chest = 4000
        purple_chest = 9000
        gold_chest = 16000
        drawn_chest = random.choices(chests_types, [75, 20, 4, 1])
        if drawn_chest == ["green_chest"]:
            print("You found green chest! there is", green_chest, "gold!")
        elif drawn_chest == ["orange_chest"]:
            print("You found orange chest! there is", orange_chest, "gold!")
        elif drawn_chest == ["purple_chest"]:
            print("You found purple chest! there is", purple_chest, "gold!")
        elif drawn_chest == ["gold_chest"]:
            print("You found gold chest! there is", gold_chest, "gold!")


movement()
