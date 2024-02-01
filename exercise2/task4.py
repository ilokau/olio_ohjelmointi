
def factorials(n: int):
    result = {}
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        result[i] = factorial

    return result

k = factorials(5)
print(k[1])  
print(k[3])  
print(k[5])
