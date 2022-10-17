# Ex2_simpl_div_N_filter. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N = '))
spisok_simpl_div_N = [x for x in range(col) if n % x == 0  and not x % spisok_simpl_div_N[i-1]    lambda n: n//x]
print(f'Это все простые делители числа {n}: {spisok_simpl_div_N}')