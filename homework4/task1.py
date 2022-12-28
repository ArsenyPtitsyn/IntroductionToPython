# Вычислить число c заданной точностью d.

import random as r

def print_with_precision(number, p):
    print(f'{number:.{p}f}')

number = r.uniform(-15, 20)
print(number)
print_with_precision(number, 5)

