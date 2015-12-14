from random import random
from random import randint
from random import randrange
numbers = []
def algo_list_write():
    for i in range(0,1000):
        numbers.append(randrange(1, 1000, randint(1, 1000)))

def search(item):
    numbers.sort()
    if numbers[int(len(numbers) / 2 - 1)] == item:
        print(numbers[int(len(numbers) / 2 -1)])
        return numbers[int(len(numbers) / 2 - 1)]