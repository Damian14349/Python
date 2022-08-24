names_and_surnames = []

with open("imionanazwiska.txt", "r") as file:
    for line in file:
        names_and_surnames.append(tuple(line.replace("\n","").split(" ")))
    print(names_and_surnames)

with open("imiona.txt", "w") as file:
    for item in names_and_surnames:
        file.write(item[0] + "\n")

with open("nazwiska.txt", "w") as file:
    for item in names_and_surnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")