# Реализуйте алгоритм перемешивания списка.

from random import randint

def create_list(size, min, max):
    result_list = [None] * size
    for i in range(size):
        result_list[i] = randint(min, max)
    return result_list

def list_shufle(initial_list):
    length = len(initial_list)
    result_list = initial_list[:]
    for i in range(length):
        random_index = randint(0, length - 1)
        temp = result_list[i]
        result_list[i] = result_list[random_index]
        result_list[random_index] = temp
    return result_list

initial_list = create_list(10, -15, 20)
print(initial_list)
result_list = list_shufle(initial_list)
print(result_list)
print(initial_list)