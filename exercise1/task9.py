import random


def randomNumber():
    number = random.randint(1, 6)
    return number


number = randomNumber()
print("Random number:", number)
