class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def search_contacts(self):
        search_name = input("Please input the name to search by: ")
        found_contact = self.phonebook.get(search_name)
        if found_contact:
            print("Number found! Search result:", found_contact.number)
        else:
            print("Contact not found.")

    def add_contact(self):
        name = input("Please enter contact name: ")
        number = input("Please enter contact number: ")
        contact = Contact(name, number)
        self.phonebook[name] = contact
        print("Contact added!")


def phonebook_menu():
    print(
        "Command options:\n1. Search contacts by name\n2. Add a new contact or update one\n3. Quit the program"
    )


print("Welcome to the phonebook!")

phonebook_instance = PhoneBook()

while True:
    phonebook_menu()

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        phonebook_instance.search_contacts()

    elif user_choice == "2":
        phonebook_instance.add_contact()

    elif user_choice == "3":
        print("Exiting phonebook.")
        break
