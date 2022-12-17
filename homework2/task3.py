# Задайте список из n чисел последовательности
# (1+\frac 1 n)^n и выведите на экран их сумму.

def create_list(n):
    list_of_sequence_elements = [None] * n
    for i in range(n):
        list_of_sequence_elements[i] = (1 + 1/(i + 1)) ** (i + 1)
    return list_of_sequence_elements

def sum_of_elements_of_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum

result_list = create_list(7)
sum = sum_of_elements_of_list(result_list)
print(sum)
