import random
from random import Random


my_list = []
for i in range(0,9): my_list.append(random.randint(0,100))
print(my_list)
my_list = [x for x in my_list if x % 2 != 0]
print(my_list)