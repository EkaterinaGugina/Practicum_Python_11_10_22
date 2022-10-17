# Ex1_differ_spisok. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.
from random import randrange
array = [randrange(1, 10) for i in range(int(input('Введите число элементов списка n = ')))]
differ_elem = list(filter(lambda x: array.count(x) == 1, array))
print(f'Первоначальный список: {array},  \n неповторяющиеся элементы: {differ_elem}')