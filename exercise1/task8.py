import random
from enum import IntEnum

player_score = 0
computer_score = 0
max_score = 3


class Choice(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


def player_choice():
    pchoice = int(input("Please make your choice. 1. Rock 2. Paper 3. Scissors: "))
    action = Choice(pchoice)
    return action


def computer_choice():
    cchoice = random.randint(1, len(Choice))
    action = Choice(cchoice)
    return action


def who_wins(player_choice, computer_choice):
    wins = {
        Choice.Rock: [Choice.Scissors],
        Choice.Paper: [Choice.Rock],
        Choice.Scissors: [Choice.Paper],
    }

    loses = wins[player_choice]
    if player_choice == computer_choice:
        print(
            f"You chose {player_choice.name}, the computer chose {computer_choice.name}. It's a tie!"
        )
    elif computer_choice in loses:
        print(
            f"You chose {player_choice.name}, the computer chose {computer_choice.name}. You win!"
        )
        global player_score
        player_score += 1

    else:
        print(
            f"You chose {player_choice.name}, the computer chose {computer_choice.name}. You lose!"
        )
        global computer_score
        computer_score += 1


while True:
    pchoice = player_choice()
    cchoice = computer_choice()

    who_wins(pchoice, cchoice)

    print(f"Player score: {player_score} \nComputer score: {computer_score}")

    if player_score == max_score or computer_score == max_score:
        if player_score > computer_score:
            print(f"Game over! Congratulations! You have won 3 times.")
        else:
            print(f"Game over! Sorry! The computer has won 3 times.")
        break
