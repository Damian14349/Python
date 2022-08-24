#

names = {"damian", "Anna", "Jaroslaw", "adrian", "Katarzyna"}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

temperature = {"t1": -10, "t2": 3, "t3": 6, "t4": 23, "t5": 12, "t6": 8, "t7": 31, "t8": 19, "t9": -3}

# podanie długości stringa
names_length = {
    name: len(name)
    for name in names
}
print(names_length)

# zmiana stringa aby zaczynały się z dużej litery
capitalized_names = {
    name.capitalize()
    for name in names
}
print(capitalized_names)
# podzielenie przez 2
devided_by_2 = {
    number: number / 2
    for number in numbers
}
print(devided_by_2)

# podanie w celsjuszach i zmiana na fahrenheity i zaokrąglenie do 1 liczby po przecinku
fahrenheit = {
    key: round(value * 1.8 + 32, 1)
    for key, value in temperature.items()
}

print("Temperature in celsiusz:", temperature)
print("Temperature in Fahrenheit:", fahrenheit)
