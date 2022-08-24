# program liczący pole powierzchni figur

import math
import figury
from enum import IntEnum

Menu_Figure = IntEnum('menu_figures', 'Square Rectangle Circle Triangle Trapeze')

menu_options = {
    1: 'Square field',
    2: 'Rectangle field',
    3: 'Circle field',
    4: 'Triangle field',
    5: 'Trapeze field',
    6: 'Exit'
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


'''
def menu(x):
    print("Choose one option:\n"
          "1 - square field\n"
          "2 - rectangle field\n"
          "3 - circle field\n"
          "4 - triangle field\n"
          "5 - trapeze field")
    if (x == '1'):
        return square_field()
    elif (x == '2'):
        return rectangle_field()
    elif (x == '3'):
        return circle_field()
    elif (x == '4'):
        return triangle_filed()
    elif (x == '5'):
        return trapeze_field()
    else:
        return
'''
while (True):
    print_menu()

    try:
        option = int(input("Choose which figure you want to count: "))
    except:
        print("Wrong input")
    if (option == Menu_Figure.Square):
        a = 0
        a = int(input("Type in square side: "))
        print("Square field:", figury.pole_kwadratu(a))
    elif (option == Menu_Figure.Rectangle):
        a, b = 0, 0
        a = int(input("Type in rectangle side length: "))
        b = int(input("Type in rectangle second side length: "))
        print("Rectangle field:", figury.pole_prostokata(a, b))
    elif (option == Menu_Figure.Circle):
        r = 0
        r = int(input("Type in circle radius: "))
        print("Circle field:", figury.pole_kola(r))
    elif (option == 4):
        a, h = 0, 0
        a = int(input("Type in triangle side: "))
        h = int(input("Type in triangle height: "))
        print("Triangle field:", figury.pole_trojkata(a, h))
    elif (option == 5):
        a, b, h = 0, 0, 0
        a = int(input("Type in trapeze side: "))
        b = int(input("Type in trapeze second side: "))
        h = int(input("Type in trapeze height: "))
        print("Trapeze field:", figury.pole_trapezu(a, b, h))
    elif (option == 6):
        break
    else:
        print("Wrong option input")
