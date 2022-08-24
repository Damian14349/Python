import json
import requests
from collections import defaultdict

site = requests.get("https://jsonplaceholder.typicode.com/todos")
tasks = site.json()
"""for entry in tasks:
    print(entry)"""


"""def count_completed_tasks(tasks):
    # utworzenie słownika aby wpisywać użytkowników i ich wyniki ukończonych zadań
    completed_tasks = dict()
    for entry in tasks:
        try:
            if (entry['completed'] == True):
                completed_tasks[entry['userId']] += 1
        # słownik na początku jest pusty, więc przy pierwszej iteracji wywala błąd, stąd except i dodanie 1 za pierwszym razem
        except KeyError:
            completed_tasks[entry['userId']] = 1

    return completed_tasks"""

def count_completed_tasks(tasks):
    # utworzenie słownika aby wpisywać użytkowników i ich wyniki ukończonych zadań
    completed_tasks = defaultdict(int)
    for entry in tasks:
        if (entry['completed'] == True):
            completed_tasks[entry['userId']] += 1

    return completed_tasks


def the_best_gets_the_cookie(completed_tasks):
    # utworzenie listy gdzie będą dodani użytkownicy z liczbą maksymalnych tasków
    users_with_maximum_completed_tasks = []
    max_amount_of_completed_tasks = max(completed_tasks.values())
    # chodzenie po listach itd. pętla ogólna: for key, value in
    for userId, number_of_completed_tasks in completed_tasks.items():
        if (number_of_completed_tasks == max_amount_of_completed_tasks):
            users_with_maximum_completed_tasks.append(userId)

    return users_with_maximum_completed_tasks


def getting_users(users_with_maximum_completed_tasks):
    u = requests.get('https://jsonplaceholder.typicode.com/users')
    users = u.json()
    winners = []
    for user in users:
        if (user['id'] in users_with_maximum_completed_tasks):
            winners.append(user['name'])

    print("The best users were:", ', '.join(winners), ". Cookie for them!")
                                    #można jeszcze użyć *winners

print(count_completed_tasks(tasks))
print(the_best_gets_the_cookie(count_completed_tasks(tasks)))
"""print("User:", the_best_gets_the_cookie(count_completed_tasks(tasks))[0],"and User:",
      the_best_gets_the_cookie(count_completed_tasks(tasks))[1],"were the best! Cookie for them!")"""
getting_users(the_best_gets_the_cookie(count_completed_tasks(tasks)))
