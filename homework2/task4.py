# Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число.

from random import randint
def create_list(n):
    result_list = [None] * n
    for i in range(n):
        result_list[i] = randint(-n, n)
    return result_list

def product_of_specified_numbers(result_list):
    n = result_list.__len__()
    with open("file1.txt", "r") as f:
        result = 1
        try:
            for line in f:
                result *= result_list[int(line)]
        except (IndexError, ValueError):
            print("Либо в списке нет элемента с таким индексом, либо в файле записано не число")
        finally:
            print(f"В файле должны содержаться только целые числа, не превосходящие по модулю {n - 1}")
            return

    return result

res_list = create_list(27)
print(res_list)
result_product = product_of_specified_numbers(res_list)
print(result_product)