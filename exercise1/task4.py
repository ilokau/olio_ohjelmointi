negnum_list = []


def isNeg(number, negnum_list):
    negnum_list.append(number)


def isZero():
    if len(negnum_list) > 0:
        print("Negative numbers entered:")
        print(negnum_list)
    else:
        print("No negative numbers were entered.")


while True:
    number = int(input("Please type a number:"))

    if number < 0:
        isNeg(number, negnum_list)

    if number == 0:
        isZero()
        break
