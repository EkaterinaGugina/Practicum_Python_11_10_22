# Ex1_confi. Вариант человек против БотаВ с интеллектом, знающего стратегию. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
from random import randint
def input_dat(name):
    x = int(input(f'{name}, введите сколько конфет возьмете (число от 1 до 28): '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, такое количество конфет брать нельзя! \
            \n Введите количество конфет (число от 1 до 28): '))
    return x
def res_out_print(name, k, count, value):
    print(f'Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.')

name1, name2 = 'Человек', 'БотВ'
value = 121
flag = randint(0, 2)             # очередность: 0 - <БотВ>, 1 - Человек
if flag:
    print(f'Первый ходит {name1}')
else:
    print(f"Первый ходит {name2}")
    # Т.к. 2021 делится на 28+1 с остатком = 20, первый игрок всегда победит, \n  если в первый раз возьмет 20, потом будет дополнять сумму взятых за xод конфет до 28+1.
    #  Для 121 конфеты победное число первого хода равно 5
k = int(121 % 29)
count1 = 0
count2 = 0
value = value - k
if flag:                   # Первый ход - случайное число
        count1 = k
        res_out_print(name1, k, count1, value)
        flag = False
else:
    count2 = k
    res_out_print(name2, k, count2, value)
    flag = False
while value > 28:
    if flag:
        k = input_dat(name1)
        count1 += k
        value -= k
        flag = False
        res_out_print(name1, k, count1, value)
    else:
        k1 = 29-k
        count2 += k1
        value -= k1
        flag = True
        res_out_print(name2, k1, count2, value)

if flag:
    print(f'Выиграл {name1}')
else:
    print(f'Выиграл {name2}')