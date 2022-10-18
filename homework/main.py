# Было:
import math
n = int(input('Enter the number: '))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial, end=' ')

# Стало:


a = int(input("Enter the number: "))
b = list(map(lambda x: math.factorial(x), range(1, a + 1)))
print(b)

# Было:

n = int(input("Enter the n: "))
list = [round((1 + 1/n)**n, 2) for n in range(1, n + 1)]
print(list)
print(round(sum(list), 2))

# Стало:

n = int(input("Enter the n: "))
print(sum([((1 + 1/n)**n) for n in range(1, n)]))
