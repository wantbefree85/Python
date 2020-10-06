from random import randint, randrange
from itertools import cycle
my_list = [randrange(50) for num in range(randint(1,20))]
print(my_list)
count = 0
for i in cycle(my_list):
    if count == len(my_list):
        break
    print(i)
    count += 1