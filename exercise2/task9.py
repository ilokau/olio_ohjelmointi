class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name, species, year_of_birth):
    return Pet(name, species, year_of_birth)


mortti = new_pet("Mortti", "Cat", 2019)
print("Name:", mortti.name)
print("Species:", mortti.species)
print("Year of birth:", mortti.year_of_birth)
