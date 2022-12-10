# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from functools import reduce
a = list(map(int, input('Введите (x,y), через пробел: ').split())) 
b = list(map(int, input('Введите (x,y), через пробел: ').split()))
res = reduce(lambda x, y: (x + y)**(1/2), (map(lambda x: (x[1] - x[0])**2, zip(a, b))))
print(round(res, 2))