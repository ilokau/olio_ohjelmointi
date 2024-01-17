step = 3

max_value = int(input("Please type the maximum value for the arithmetic progression:"))


def arithmetic_progression(step, max_value):
    ap = list(range(step, max_value + 1, step))
    return ap


def ap_length(ap):
    return len(ap)


def ap_sum(ap):
    return sum(ap)


def ap_square_sum(ap):
    return sum(i**2 for i in ap)


print(arithmetic_progression(step, max_value))
print("Number of terms:", ap_length(arithmetic_progression(step, max_value)))
print("Sum of terms:", ap_sum(arithmetic_progression(step, max_value)))
print("Sum of squared terms:", ap_square_sum(arithmetic_progression(step, max_value)))
