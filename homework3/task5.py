# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

import random as r

def fibonacci(number):
    if number >= 0:
        if number == 0:
            return 0
        if number == 1 or number == 2:
            return 1
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)
    else:
        return int(fibonacci(-number) * (-1) ** (number + 1))

def create_list_of_fibonacci(number):
    length = 2 * number + 1
    fibonacci_list = [None] * (length)
    for i in range(length):
        fibonacci_list[i] = fibonacci(i - number)
    return fibonacci_list

number = r.randint(5, 20)
print(number)
fibonacci_list = create_list_of_fibonacci(number)
print(fibonacci_list)