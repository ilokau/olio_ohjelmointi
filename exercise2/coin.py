import random


class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss_the_coin(self):
        coin_value = random.randint(0, 4)
        if coin_value == 0:
            self.sideup = "Heads"
        elif coin_value == 1:
            self.sideup = "Tails"
        elif coin_value == 2:
            self.sideup = "Upright"
        elif coin_value == 3:
            self.sideup = "Rhole"
        else:
            self.sideup = "Whole"

    def get_sideup(self):
        return self.sideup


def main():
    thrown_coin = Coin()

    print("This side is up:", thrown_coin.get_sideup())

    print("Tossing the coin...")
    thrown_coin.toss_the_coin()

    if thrown_coin.get_sideup() == "Heads" or thrown_coin.get_sideup() == "Tails":
        print("Now this side is up:", thrown_coin.get_sideup())
    elif thrown_coin.get_sideup() == "Upright":
        print("The coin landed upright, it's neither heads nor tails!")
    elif thrown_coin.get_sideup() == "Rhole":
        print("The coin fell on the ground and disappeared in a rabbit hole!")
    elif thrown_coin.get_sideup() == "Whole":
        print("The coin defied gravity and got lost in a wormhole in space!")


# Calling the main function
main()
