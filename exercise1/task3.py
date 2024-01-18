import random

number_list = []
string_list = []

while len(number_list) < 10:
    number = input("Please type a number:")
    number_list.append(number)

while len(string_list) < 10:
    string = input("Please type a word:")
    string_list.append(string)

print(number_list)
print(string_list)

number_list.sort()
string_list.sort()

print("Number list in ascending order:")
print(number_list)

print("String list in alphabetical order:")
print(string_list)

print("Adding random numbers to numbers list.")
for i in range(0, 10):
    number = random.randint(1, 100)
    number_list[i] = number

print("Number list in ascending order:")
number_list.sort()
print(number_list)
