class NumberStats:
    def __init__(self):
        # no need to add any new varibales here, just change the
        # initialization of the self.numbers variable.
        self.numbers = []
        self.count = 0
        self.sum = 0

    # Parts 1 and 2 functions
    def add_number(self, number: int):
        self.sum += number
        self.count += 1
        self.numbers.append(number)
        return self.numbers

    def count_numbers(self):
        count = len(self.numbers)
        return count

    def get_sum(self):
        return self.sum

    def avg(self):
        if self.count == 0:
            return 0
        return self.sum / self.count


if __name__ == "__main__":
    # Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    # Part 2 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.avg())


# Part 3 main function
stats = NumberStats()

while True:
    userinput = int(input("Please type in integer numbers. Type -1 to finish."))
    if userinput == -1:
        break
    stats.add_number(userinput)

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.avg())
