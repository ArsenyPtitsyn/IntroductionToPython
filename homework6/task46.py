# Найти произведение пар чисел списка
# (парой считаем первый и последний, второй предпоследний и тд)

from random import randint

start_list = [randint(-50, 100) for i in range(randint(1, 30))]

res_list = list(map(lambda i: start_list[i] * start_list[len(start_list) - 1 - i], range(0, len(start_list) // 2)))
if len(start_list) % 2 == 1:
    res_list.append(start_list[len(start_list) // 2])

sum_of_elements = lambda list: sum(list)

print(start_list)
print(res_list)
print(sum_of_elements(res_list))