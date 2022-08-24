import json
import requests
import webbrowser
from enum import Enum
import pprint

def menu():
    Menu = Enum('Menu', 'abys aege abob acur beng sibe')

    choice = int(input("Choose option:\n"
                       "1. Abyssinian\n"
                       "2. Aegean\n"
                       "3. American Bobtail\n"
                       "4. American Curl\n"
                       "5. Bengal\n"
                       "6. Siberian\n"))

    animal_type = Menu(choice).name
    #animal_type = 'beng'

    params = {
        "limit": 3,
        "id": animal_type
    }
    if choice == Menu.abys.value:
        request = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=abys", params)
    elif choice == Menu.aege.value:
        request = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=aege", params)
    elif choice == Menu.abob.value:
        request = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=abob", params)
    elif choice == Menu.acur.value:
        request = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=acur", params)
    elif choice == Menu.beng.value:
        request = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=beng", params)
    elif choice == Menu.sibe.value:
        request = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=sibe", params)

    try:
        facts = request.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")
    else:
        for animal in facts:
            webbrowser.open_new_tab(animal["url"])
            #pprint.pprint(facts)

menu()
"""params = {
    "limit": 3,
    "id": 'beng'
}
request = requests.get("https://api.thecatapi.com/v1/images/search?", params)

try:
    facts = request.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for breed in facts['url']:
        pprint.pprint(facts)"""
