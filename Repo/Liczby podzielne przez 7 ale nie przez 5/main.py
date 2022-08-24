# Znajdź liczby od 100 do 470 włącznie, które są podzielne przez 7, ale jednocześnie nie są podzielne przez 5

def printer():
    for number in numbers:
        # znak specjalny end - kończy zdanie jak chcemy, nie nową linią jak standardowo
        print(number, end=" ")
    print('')


# generator
numbers = (
    number
    for number in range(99, 471)
    if (number % 7 == 0 and number % 5 != 0)
)
printer()

# wyrażenie listowe
numbers = [
    number
    for number in range(99, 471)
    if (number % 7 == 0 and number % 5 != 0)
]
printer()

# wyrażenie zbioru
numbers = {
    number
    for number in range(99, 471)
    if (number % 7 == 0 and number % 5 != 0)
}
printer()
