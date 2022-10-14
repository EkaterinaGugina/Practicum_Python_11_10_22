# # Ex1_confi. Вариант человек против БотаВ с интеллектом, знающего стратегию. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# from random import randint
# def input_dat(name):
#     x = int(input(f'{name}, введите сколько конфет возьмете (число от 1 до 28): '))
#     while x < 1 or x > 28:
#         x = int(input(f'{name}, такое количество конфет брать нельзя! \
#             \n Введите количество конфет (число от 1 до 28): '))
#     return x

# def res_out_print(name, k, count, value):
#     print(f'Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.')

# name1, name2 = 'Человек', 'БотВ'
# value = 121
# flag = randint(0, 2)             # очередность: 0 - <БотВ>, 1 - Человек
# if flag:
#     print(f'Первый ходит {name1}')
# else:
#     print(f"Первый ходит {name2}")

#     # Т.к. 2021 делится на 28 с остатком = 15, первый игрок всегда победит, \n
#     # если в первый раз возьмет 15, потом будет дополнять сумму взятых за xод конфет до 28+1.
#     #  Для 121 конфеты победное число первого хода равно 9
# k = int(121 % 28)
# count1 = 0
# count2 = 0
# value = value - k
# if flag:                   # Первый ход - случайное число
#         count1 = k
#         res_out_print(name1, k, count1, value)
#         flag = False
# else:
#     count2 = k
#     res_out_print(name1, k, count2, value)
#     flag = False
# while value > 28:
#     if flag:
#         k = input_dat(name1)
#         count1 += k
#         value -= k
#         flag = False
#         res_out_print(name1, k, count1, value)
#     else:
#         k1 = 29-k
#         count2 += k1
#         value -= k1
#         flag = True
#         res_out_print(name2, k1, count2, value)

# if flag:
#     print(f'Выиграл {name1}')
# else:
#     print(f'Выиграл {name2}')



# вариант человек против бота без интеллекта:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите сколько конфет возьмете (число от 1 до 28): "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, такое количество конфет брать нельзя! \
            \n Введите количество конфет (число от 1 до 28): "))
    return x


def res_out_print(name, k, count, value):
    print(f"Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.")

name1, name2 = "Человек", "БотA"
value = 2021
flag = randint(0,2)  # очередность: 0 - человек, 1 - БотА
if flag:
    print(f"Первый ходит {name1}")
else:
    print(f"Первый ходит {name2}")

k = int(121 % 28)
count1 = 0 
count2 = 0
if flag:                   # Первый ход - случайное число 
        print(f'{name1}, если хочешь победить, бери {k} штук в первый раз, а потом смотри подсказки на экране')
        count1 += k
        value -= k
        flag = False
        res_out_print(name1, k, count1, value)
else:
    flag = False
    res_out_print(name2, k, count2, value)

while value > 28:
    if flag:
        k = input_dat(name1)
        count1 += k
        value -= k
        flag = False
        res_out_print(name1, k, count1, value)
    else:
        k = randint(1,29)
        count2 += k
        value -= k
        flag = True
        res_out_print(name2, k, count2, value)

if flag:
    print(f"Выиграл {name1}")
else:
    print(f"Выиграл {name2}")
    
    
    
    
# вариант человек против человека (не знают стратегию):
# def input_dat(name):
#     x = int(input(f"{name}, введите сколько конфет возьмете (число от 1 до 28): "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, такое количество конфет брать нельзя! \
#             \n Введите количество конфет (число от 1 до 28): "))
#     return x

# def res_out_print(name, k, count, value):
#     print(f"Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.")

# name1, name2 = "Первый игрок", "Второй игрок"
# value = 2021
# flag = randint(0,2)             # очередность: 0 - 2человек, 1 - 1человек
# if flag:
#     print(f"Первый ходит {name1}")
# else:
#     print(f"Первый ходит {name2}")

# count1 = 0 
# count2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(name1)
#         count1 += k
#         value -= k
#         flag = False
#         res_out_print(name1, k, count1, value)
#     else:
#         k = input_dat(name2)
#         count2 += k
#         value -= k
#         flag = True
#         res_out_print(name2, k, count2, value)

# if flag:
#     print(f"Выиграл {name1}")
# else:
#     print(f"Выиграл {name2}")
    



# Вариант человек против БотаВ с интеллектом, знающего стратегию. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# def input_dat(name):
#     x = int(input(f"{name}, введите сколько конфет возьмете (число от 1 до 28): "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, такое количество конфет брать нельзя! \
#             \n Введите количество конфет (число от 1 до 28): "))
#     return x

# def res_out_print(name, k, count, value):
#     print(f"Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.")

# name1, name2 = "Человек", "БотВ"
# value = 121
# flag = randint(0,2)             # очередность: 0 - БотВ, 1 - Человек
# if flag:
#     print(f"Первый ходит {name1}")
# else:
#     print(f"Первый ходит {name2}")
    
#     # Т.к. 2021 делится на 28 с остатком = 15 первый игрок всегда победит, если в первый раз возьмет 15, потом будет дополнять сумму взятых за кон конфет до 28+1.
#     #  Для 121 конфеты число первого хода равно 9
# k = int(121 % 28)
# count1 = k
# value = value - k
# if flag:                   # Первый ход - случайное число 
#         flag = False
#         res_out_print(name1, k, count1, value)
# else:
#     flag = False
#     res_out_print(name2, k, count2, value)
# while value > 28:
#     if flag:
#         k = input_dat(name1)
#         count1 += k
#         value -= k
#         flag = False
#         res_out_print(name1, k, count1, value)
#     else:
#         k = input_dat(name2)
#         count2 += k
#         value -= k
#         flag = True
#         res_out_print(name2, k, count2, value)

# if flag:
#     print(f"Выиграл {name1}")
# else:
#     print(f"Выиграл {name2}")