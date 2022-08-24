import json
from enum import Enum
import requests
from pprint import pprint


def menu():
    Menu = Enum('Menu', 'cat dog')

    choice = int(input("Choose option:\n"
                       "1. cat\n"
                       "2. dog\n"))

    animal_type = Menu(choice).name

    params = {
        "amount": 5,
        "animal_type": animal_type
    }

    if choice == Menu.cat.value:
        request = requests.get("https://cat-fact.herokuapp.com/facts/random", params)
    elif choice == Menu.dog.value:
        request = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

    try:
        facts = request.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")
    else:
        for animal in facts:
            print(animal["text"])

menu()


"""params = {
        "amount": 2,
        "animal_type": "cat"
    }

request = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

try:
    facts = request.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for animal in facts:
        pprint(animal["text"])"""