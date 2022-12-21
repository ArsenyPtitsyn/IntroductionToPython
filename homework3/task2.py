# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.

import random as r
def create_list(n, min, max):
    new_list = [None] * n
    for i in range(n):
        new_list[i] = r.randint(min, max)
    return new_list

def create_result_list(initial_list):
    k = len(initial_list) // 2
    if len(initial_list) % 2 != 0:
        k += 1
    result_list = [None] * k
    for i in range(k):
        result_list[i] = initial_list[i] * initial_list[len(initial_list) - i - 1]
    if len(initial_list) % 2 != 0:
        result_list[k - 1] = initial_list[k - 1]
    return result_list

my_list = create_list(14, -20, 20)
print(my_list)
result_list = create_result_list(my_list)
print(result_list)