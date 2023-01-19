# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
from random import randint
import math as m

get_point = lambda dimensions: [randint(-100, 100) for index in range(dimensions)]

distance = lambda p1, p2: m.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

point1 = get_point(2)
point2 = get_point(2)
print(point1)
print(point2)
print(distance(point1, point2))