import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.current_side = 1

    def roll(self):
        self.current_side = random.randint(1, self.sides)

    def get_current_side(self):
        return self.current_side


def roll_dice(dice_list):
    for dice in dice_list:
        dice.roll()


def sum_of_rolls(dice_list):
    return sum(dice.get_current_side() for dice in dice_list)


def dice_game(num_rounds, num_dice):

    print("Dice game")
    print("Throwing", num_dice, "dice per round for", num_rounds, "rounds.")

    dices = [Dice() for _ in range(num_dice)]

    best_sum = 0

    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num} - Rolling the dice...")
        roll_dice(dices)
        roll_list = [dice.get_current_side() for dice in dices]
        round_sum = sum_of_rolls(dices)

        print("Rolls:", roll_list)
        print("Round Sum:", round_sum)

        if round_sum > best_sum:
            best_sum = round_sum

        elif round_sum == best_sum:
            print("\nTie! Doing a tiebreaker roll:")
            roll_dice(dices)
            tiebreaker_rolls = [dice.get_current_side() for dice in dices]
            print("Tiebreaker Roll:", tiebreaker_rolls)
            round_sum = sum(tiebreaker_rolls)
            print("Round Sum", round_sum)

    print(f"\nHighest Round Score: {best_sum}. Game Over!")


dice_game(3, 3)
