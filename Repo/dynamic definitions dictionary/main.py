# dynamic definitions dictionary

definicions = {}

while (True):
    print("1 - Add definition\n"
          "2 - Find definition\n"
          "3 - Erase definition\n"
          "4 - Show definitions\n"
          "5 - Close")

    choose = input("Choose option: ")
    if (choose == "1"):
        key = input("Write key: ")
        definiction = input("Write your definition: ")
        definicions[key] = definiction
        print("Definition added")
    elif (choose == "2"):
        key = input("Type key to find: ")
        if key in definicions:
            print(definicions[key])
        else:
            print("Key doesn't exist")
    elif (choose == "3"):
        key = input("Write key to erase: ")
        if key in definicions:
            definicions.pop(key)
        else:
            print("Key doesnt' exist")
    elif (choose == "4"):
        print(definicions)
    else:
        print("End")
        break