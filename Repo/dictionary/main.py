# poruszanie się po słowniku i listach

dictionary = {
    "93102602656": {"name": "Damian", "age": 28, "sex": "male"},
    "94112602656": {"name": "Lukasz", "age": 33, "sex": "male"},
    "98126026555": {"name": "Anna", "age": 54, "sex": "female"},
    "74112602656": {"name": "Karolina", "age": 76, "sex": "female"},
    "83126026789": {"name": "Adrian", "age": 12, "sex": "male"},
    "93126020932": {"name": "Joanna", "age": 31, "sex": "female"},
    "93086020981": {"name": "Zdzislaw", "age": 29, "sex": "male"}
}
'''
#przechodzenie po słowniku za pomocą pętli
for key in dictionary:
    print("pesel:",key)
    for secondary_key in dictionary[key]:
        print(secondary_key,dictionary[key][secondary_key])
'''

#przechodzenie po słowniku również za pomocą pętli ale przy wykorzystaniu funkcji items()
for pesel, dictionary in dictionary.items():
    print(pesel, dictionary)
