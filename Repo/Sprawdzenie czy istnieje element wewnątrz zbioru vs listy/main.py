
import random

def is_element_in(input):
    input = random.randint(-10, 10)
    input1 = int(input("Type in your number"))
    set_container = {i for i in range(random.randint(-10, 10))}
    list_container = [i for i in range(random.randint(-10, 10))]
    print(set_container)
    print(list_container)
    while (True):
        if input1 in set_container:
            return "in set YES"
            continue
        elif input1 in list_container:
            return "in list YES"
            continue
        elif input1 not in set_container:
            return "in set NO"
            continue
        elif input1 not in list_container:
            return "in list NO"

print(is_element_in(input))



