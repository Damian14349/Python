#funkcja symulująca lotto
import random


def lotto(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

lotto(6, 49)