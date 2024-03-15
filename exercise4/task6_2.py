import random  # tiebreaker puuttuu


class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.current_side = 1

    def roll(self):
        self.current_side = random.randint(1, self.sides)

    def get_current_side(self):
        return self.current_side


class Player:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self.dice = Dice()
        self.roll_list = []
        self.pet = None

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_pet(self):
        return self.pet

    def set_pet(self, mammal):
        self.pet = mammal

    def __str__(self):
        return f"Player: {self._name}, ID: {self._id}, Pet: {self.pet}"

    def set_name(self, new_name):
        self._name = new_name

    def set_id(self, new_id):
        self._id = new_id

    def __str__(self):
        return f"Player: {self._name,}, ID: {self._id}, Pet: {self.pet}"

    def player_roll(self):
        self.dice.roll()

    def get_player_dice_side(self):
        return self.dice.get_current_side()


class Mammal:
    def __init__(self, mammal_id, species, name, size, weight):
        self.mammal_id = mammal_id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

    def __str__(self):
        return f"{self.name} (ID: {self.mammal_id}, Species: {self.species}, Size: {self.size}, Weight: {self.weight}"


def pet_assignment(players):
    mammals_list = [
        {"species": "Elephant", "name": "Dumbo", "size": "Very Large", "weight": 500},
        {"species": "Dog", "name": "Musti", "size": "Large", "weight": 25},
        {"species": "Cat", "name": "Mirri", "size": "Small", "weight": 10},
        {"species": "Bird", "name": "Polli", "size": "Small", "weight": 5},
    ]

    players_sorted = sorted(
        players, key=lambda x: sum(x.roll_list), reverse=True
    )  # sorting based on rolls after dice game
    player_ranking = {
        player: rank for rank, player in enumerate(players_sorted, 1)
    }  # ranking players based on the rolls sort

    for player in players:  # assigning pet based on ranking
        rank = player_ranking[player]
        mammal_info = mammals_list[rank - 1]
        player_pet = Mammal(player.get_id(), **mammal_info)
        player.set_pet(player_pet)


def sum_of_rolls(dice_list):
    return sum(dice.get_current_side() for dice in dice_list)


def dice_game(players, num_rounds, num_dice):
    # dice_list = [player.dice for player in players]

    print("Dice game")
    print("Throwing", num_dice, "dice per round for", num_rounds, "rounds.")

    best_sum = 0
    best_player = None

    for i in range(num_rounds):
        print(f"Round {i + 1}")
        for player in players:
            player.roll_list = []

            for j in range(num_dice):
                player.player_roll()
                player.roll_list.append(player.get_player_dice_side())

            current_sum = sum(player.roll_list)

            print(
                f"Player {player.get_name()} rolls: {player.roll_list} = {current_sum}"
            )
            if current_sum > best_sum:
                best_sum = current_sum
                best_player = player.get_name()

        # print("Player sum:", current_sum)

    print("\nHighest sum:", best_sum)
    print(f"Player {best_player} wins with the highest sum of", best_sum)

    players_sorted = sorted(players, key=lambda x: sum(x.roll_list), reverse=True)
    pet_assignment(players_sorted)

    print("\nPet selection results:")
    for player in players:
        print(f"{player}")

    """for player in players:
        mammal_info = random.choice(mammals_list)
        player_pet = Mammal(player.get_id(), **mammal_info)
        player.set_pet(player_pet)
        print(f"\n{player}")"""


player1 = Player("Ethan", id=1)
player2 = Player("Jason", id=2)
player3 = Player("Shaun", id=3)

players_list = [player1, player2, player3]

# Example usage
dice_game(players_list, num_rounds=3, num_dice=3)
