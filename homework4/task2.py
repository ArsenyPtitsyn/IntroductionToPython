# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

import random as r
import math as m

def is_prime_number(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

def prime_numbers_equal_or_less_then(number):
    prime_numbers = list()
    for i in range(2, number + 1):
        if is_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers

def prime_factors_of_number(number):
    prime_factors = list()
    for i in prime_numbers_equal_or_less_then(number):
        if number % i == 0:
            prime_factors.append(i)
    return prime_factors


number = r.randint(1, 1000)
print(number)
print(prime_factors_of_number(number))
