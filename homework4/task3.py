# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

import random as r

def create_list_of_random_numbers(size, min, max):
    random_list = [None] * size
    for i in range(size):
        random_list[i] = r.randint(min, max)
    return random_list

def create_list_with_non_repiting_elements(random_list):
    result_list = []
    for i in random_list:
        if i not in result_list:
            result_list.append(i)
    return result_list

random_list = create_list_of_random_numbers(20, -5, 5)
print(random_list)
non_repeat_list = create_list_with_non_repiting_elements(random_list)
print(non_repeat_list)