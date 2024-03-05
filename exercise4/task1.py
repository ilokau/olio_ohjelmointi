class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list):
        counts = {}
        # dictionary that counts how many times each number appears on the list
        for number in my_list:
            counts[number] = counts.get(number, 0) + 1

        # finding the number with the most appearances (highest count)
        most_frequent_number = max(counts, key=counts.get)
        return most_frequent_number

    @classmethod
    def doubles(cls, my_list):
        counts = {}
        for number in my_list:
            counts[number] = counts.get(number, 0) + 1

        # counting how many unique numbers appear on the list at least twice
        doubles_count = sum(1 for count in counts.values() if count >= 2)
        return doubles_count


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
