# suma wszystkich liczb do liczby podanej przez użytkownika

import time


def sum_with_loop(number):
    sum = 0

    for number in range(1, number + 1):
        sum = sum + number

    return sum


def sum_with_list(number):
    return sum([number for number in range(1, number + 1)])


def sum_with_dictionary(number):
    return sum({number for number in range(1, number + 1)})


def sum_with_generator(number):
    return sum((number for number in range(1, number + 1)))


def sum_arithmetic(number):
    return (1 + number) / 2 * number


def perf_timer(start):
    end = time.perf_counter()
    return end - start


def function_performance(func, number):
    start = time.perf_counter()
    func(number)
    end = time.perf_counter()
    return end - start


number = int(input('Type number: '))

'''
#timer ustawiony przy printach - mało eleganckie rozwiązanie
start = time.perf_counter()
print(sum_with_loop(number))
print(perf_timer(start))

start = time.perf_counter()
print(sum_with_list(number))
print(perf_timer(start))

start = time.perf_counter()
print(sum_with_dictionary(number))
print(perf_timer(start))

start = time.perf_counter()
print(sum_with_generator(number))
print(perf_timer(start))

print(sum_arithmetic(number))
print(perf_timer(start))

'''

#eleganckie rozwiązanie z timerem w osobnej metodzie
print(function_performance(sum_with_list, number))
print(function_performance(sum_with_list, number))
print(function_performance(sum_with_dictionary, number))
print(function_performance(sum_with_generator, number))
print(function_performance(sum_arithmetic, number))
