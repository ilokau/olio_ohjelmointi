
class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
    
dune = Book("Dune", "Frank Herbert", "Sci-fi", 1965)
karenina = Book("Anna Karenina", "Leo Tolstoy", "Drama", 1878)

print(f"{dune.author}: {dune.name} ({dune.year})")
print(f"The genre of the boook {karenina.name} is {karenina.genre}")

    
