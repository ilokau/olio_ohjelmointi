# part 1 code
class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def name(self):
        return self._name

    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"


# part 2 code
class Suitcase:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._items = []

    def add_item(self, item):
        if (
            sum(item.weight() for item in self._items) + item.weight()
            <= self._max_weight
        ):
            self._items.append(item)
        else:
            print("Maximum weight exceeded, can't add item.")

    def weight(self):
        return sum(item.weight() for item in self._items)

    def __str__(self):
        item_amount = len(self._items)

        if item_amount == 1:
            return f"{item_amount} item ({self.weight()} kg)"
        else:
            return f"{item_amount} items ({self.weight()} kg)"

    # part 4
    def print_items(self):
        for item in self._items:
            print(f"{item.name()} ({item.weight()} kg)")

    # part 5
    def heaviest_item(self):
        if not self._items:
            return None
        return max(self._items, key=lambda item: item.weight())


class CargoHold:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._suitcases = []

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() <= self._max_weight:
            self._suitcases.append(suitcase)

    def weight(self):
        return sum(suitcase.weight() for suitcase in self._suitcases)

    def __str__(self):
        num_suitcases = len(self._suitcases)
        remaining_space = self._max_weight - self.weight()
        return f"{num_suitcases} {'suitcase' if num_suitcases == 1 else 'suitcases'}, space for {remaining_space} kg"

    def print_items(self):
        for suitcase in self._suitcases:
            suitcase.print_items()


# Example usage:
"""book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

print("Name of the book:", book.name())
print("Weight of the book:", book.weight(), "g")

print("Book:", book)
print("Phone:", phone)

suitcase = Suitcase(1000)
print(suitcase)

suitcase.add_item(book)
print(suitcase)

suitcase.add_item(phone)
print(suitcase)

suitcase.add_item(brick)
print(suitcase)

print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} g")"""

"""cargo_hold = CargoHold(100)
print(cargo_hold)

book = Item("ABC Book", 0.2)
phone = Item("Nokia 3210", 0.1)
brick = Item("Brick", 0.4)

adas_suitcase = Suitcase(1)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase = Suitcase(1)
peters_suitcase.add_item(brick)

cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)

cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)"""

book = Item("ABC Book", 0.2)
phone = Item("Nokia 3210", 0.1)
brick = Item("Brick", 0.4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
