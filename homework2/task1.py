# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

def split_real_number(number):
    return number.split(".")

def sum_of_digits_of_number(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

x = input("Введите вещественное число используя точку для разделения целой и дробной части: ")
list = split_real_number(x)
sum = 0
for i in range(2):
    sum += sum_of_digits_of_number(list[i])
print(sum)