# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.

import random as r

def create_new_list(size, min, max):
    new_list = [None] * size
    for i in range(size):
        new_list[i] = r.randint(min, max)
    return new_list

def create_polynom(degree, min, max):
    list_of_coefficients = create_new_list(degree + 1, min, max)
    s: str = ""
    for i in range(degree):
        if list_of_coefficients[i] == 0:
            continue
        s += f'{list_of_coefficients[i]}*x^{degree - i} + '
    if list_of_coefficients[degree] == 0:
        s = s[:-2] + s[-1:]
    else:
        s += f"{list_of_coefficients[degree]}"
    return s

def write_polynom_to_file(file_name, polygon):
    with open(file_name, 'w') as data:
        data.write(polygon)

polygon = create_polynom(5, 0, 3)
print(polygon)
write_polynom_to_file("file.txt", polygon)