# Ex3_sum_elem_not_mod_2 Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> (на нечётных позициях элементы 3 и 9) ответ: 12
from random import randrange

array = [randrange(-9, 10) for i in range(int(input('Введите число элементов списка n = ')))]
# array = [2, 3, 5, 9, 3] 
sum = sum([array[i] for i in range(len(array)) if i % 2 != 0])         
print(f'{array} ---> сумма элементов на нечётных позициях равна {sum}')


# Создание списка от -N до N
# n = 9
# list_n = [i for i in range(- n, n + 1)]
# print(list_n)