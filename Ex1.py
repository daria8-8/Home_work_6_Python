# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
lst = list(map(int, input('Введите числа, через пробел: ').split()))
print(list(filter(lambda x: x==max(lst),lst)))
