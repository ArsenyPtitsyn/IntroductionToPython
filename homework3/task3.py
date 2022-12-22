# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

import random as r

def create_list_of_real_numbers(n, max):
    initial_list = [None] * n
    for i in range(n):
        initial_list[i] = max * r.random()
    return initial_list

def get_fractional_part(number):
    int_and_fract = str(number).split(".")
    return float("0." + int_and_fract[1])

def create_list_of_fractional_parts(initial_list):
    length = len(initial_list)
    fractional_list = [None] * length
    for i in range(length):
        fractional_list[i] = get_fractional_part(initial_list[i])
    return fractional_list

def max_fractional_part(fractional_list):
    length = len(fractional_list)
    max = fractional_list[0]
    for i in range(1, length):
        if fractional_list[i] > max:
            max = fractional_list[i]
    return max

def min_fractional_part(fractional_list):
    length = len(fractional_list)
    min = fractional_list[0]
    for i in range(1, length):
        if fractional_list[i] < min:
            min = fractional_list[i]
    return min

def difference_of_max_and_min(fractional_list):
    return max_fractional_part(fractional_list) - min_fractional_part(fractional_list)

initial_list = create_list_of_real_numbers(6, 10)
print(initial_list)
fractional_list = create_list_of_fractional_parts(initial_list)
print(fractional_list)
result = difference_of_max_and_min(fractional_list)
print(result)

