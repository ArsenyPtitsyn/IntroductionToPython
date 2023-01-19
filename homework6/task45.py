# Найти сумму чисел списка стоящих на нечетной позиции.

from random import randint

get_list = lambda n: [randint(-55, 55) for i in range(n)]

start_list = get_list(15)
print(start_list)
res_list = list(map(lambda i: start_list[i], range(0, len(start_list), 2)))
print(res_list)