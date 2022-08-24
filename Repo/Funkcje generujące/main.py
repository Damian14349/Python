def multiply_generator():
    number = 0
    while True:
        number += 1
        yield number * number


def list_appender(number):
    generated_numbers = []
    number_generator = multiply_generator()
    for _ in range(20):
        generated_numbers.append(next(number_generator))
    print("Wygenerowane 20 liczb w liście:", generated_numbers)
    for _ in range(30):
        generated_numbers.append(next(number_generator))
    print("Wygenerowanie kolejnych 30 liczb i dodanie ich do tej samej liczby", generated_numbers)


list_appender(multiply_generator())