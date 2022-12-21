# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random as r
def create_list(n):
    initial_list = [None] * n
    for i in range(n):
        initial_list[i] = r.randint(-100, 100)
    return initial_list

def sum_of_elements_with_odd_indexes(spec_list):
    sum = 0
    for i in range(1, len(spec_list), 2):
        sum += spec_list[i]
    return sum

specified_list = create_list(16)
print(specified_list)
sum = sum_of_elements_with_odd_indexes(specified_list)
print(sum)
