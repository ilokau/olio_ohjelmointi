class Computer:
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed


class LaptopComputer(Computer):
    def __init__(self, model, speed, weight):
        super().__init__(model, speed)
        self._weight = weight

    def __str__(self):
        return f"{self._model}, {self._speed} MHz, {self._weight} kg"


laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)
