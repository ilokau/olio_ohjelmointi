class Person:
    def __init__(self, name):
        self.__name = name
        self.__number = []
        self.__address = None

    def name(self):
        return self.__name

    def number(self):
        return self.__number

    def address(self):
        return self.__address

    def add_number(self, number):
        self.__number.append(number)

    def add_address(self, address):
        self.__address = address


class Phonebook:
    def __init__(self):
        self.__persons = {}

    def add_person(self, name):
        if name not in self.__persons:
            self.__persons[name] = Person(name)

    def add_number(self, name: str, number: str):
        self.add_person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        self.add_person(name)
        self.__persons[name].add_address(address)

    def get_person(self, name: str):
        return self.__persons.get(name)

    def all_info(self):
        return {
            name: {"number": person.number(), "address": person.address()}
            for name, person in self.__persons.items()
        }


class PhoneBookApplication:
    def __init__(self):
        self.__book = Phonebook()

    def instructions(self):
        print("commands: ")
        print("0 quit")
        print("1 add number")
        print("2 add address")
        print("3 search")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__book.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__book.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__book.get_person(name)
        if person is None:
            print("Person not found")
            return
        print("Name:", person.name())
        print("Number:", person.number())
        print("Address:", person.address())

    def run(self):
        self.instructions()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.add_address()
            elif command == "3":
                self.search()
            else:
                self.instructions()


"""person = Person("Eric")
print(person.name())
print(person.number())
print(person.address())
person.add_number("040-123456")
person.add_address("Mannerheimintie 10 Helsinki")
print(person.number())
print(person.address())"""

# test the code
application = PhoneBookApplication()
application.run()
