from random import randint

def random_even(a, b):
    result = 1
    while result % 2 != 0:
        result = randint(a, b)
    return result

print(random_even(0, 100))

