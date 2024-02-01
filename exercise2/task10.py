class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


def books_of_genre(books, genre):
    # Use a list comprehension to filter books by genre
    return [book for book in books if book.genre == genre]


dune = Book("Dune", "Frank Herbert", "Sci-fi", 1965)
karenina = Book("Anna Karenina", "Leo Tolstoy", "Drama", 1878)
hitchhiker = Book(
    "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Sci-fi", 1979
)

books = [dune, karenina, hitchhiker]
sci_fi_books = books_of_genre(books, "Sci-fi")

print("\nBooks in the Sci-fi genre:")
for book in sci_fi_books:
    print(f"{book.author}: {book.name} ({book.year})")
