# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input("Введите натуральное число: "))
factorials = [1] * n
for i in range(n):
    for j in range(1, i + 2):
        factorials[i] *= j
print(factorials)