for fizz_buzz in range(1, 101):
    if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
        print(fizz_buzz, "FizzBuzz")
    elif fizz_buzz % 3 == 0:
        print(fizz_buzz, "Fizz")
        continue
    elif fizz_buzz % 5 == 0:
        print(fizz_buzz, "Buzz")
        continue
