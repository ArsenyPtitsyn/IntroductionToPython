# Реализуйте алгоритм перемешивания списка.

from random import randint

# def create_list(n, min, max):
#     result_list = [None] * n
#     for i in range(n):
#         result_list[i] = randint(min, max)
#     return result_list
#
# def list_shufle(initial_list):
#     length = initial_list.__len__()
#     result_list = [None] * length
#     for i in range(length):
#         j = randint(0, length)
#         if result_list[j] == None:
l = list(range(1, 6))

for i in range(1, 6):
    j = randint(1, 5)
