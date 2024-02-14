
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.persons = []
        
    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if self.is_empty():
            print("The room is empty.")
        else:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm.")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")
                
    def shortest(self):
        if self.is_empty():
            return None
        else:
            return min(self.persons, key=lambda person: person.height)
        
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person


room = Room() 
print("Is the room empty?", room.is_empty()) 
room.add(Person("Lea", 183)) 
room.add(Person("Kenya", 172)) 
room.add(Person("Ally", 166)) 
room.add(Person("Nina", 162)) 
room.add(Person("Dorothy", 175)) 
print("Is the room empty?", room.is_empty()) 
room.print_contents()
print()
print("Is the room empty?", room.is_empty()) 
print("Shortest:", room.shortest()) 
print() 
room.print_contents()
print()
removed = room.remove_shortest() 
print(f"Removed from room: {removed.name}") 
print() 
room.print_contents()