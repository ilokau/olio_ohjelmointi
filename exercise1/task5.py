negnum_list = []
even_count = 0


def countEven(number):
    global even_count
    even_count += 1


def isNeg(number, negnum_list):
    negnum_list.append(number)


def isZero():
    if len(negnum_list) > 0:
        print("Negative numbers entered:")
        print(len(negnum_list))
        print("The number of even numbers:", even_count)
    else:
        print("No negative numbers were entered.")
        print("The number of even numbers:", even_count)


while True:
    number = int(input("Please type a number:"))

    if number < 0:
        isNeg(number, negnum_list)

    if number == 0:
        isZero()
        break

    if number % 2 == 0:
        countEven(number)
