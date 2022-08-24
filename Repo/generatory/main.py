#wyrażenia generujące
import sys

#zsumowanie liczb od 0 do 100 podniesione do potęgi drugiej
numbers_generator = (elements**2
                     for elements in range(101)
                    )

print(sys.getsizeof(numbers_generator))

'''
#wypisanie elementów spotęgowanych bez sumy
for elements in numbers_generator:
    print(elements)
'''
#suma spotęgowanych elementów
print("suma spotęgowanych elementów:",sum(numbers_generator))