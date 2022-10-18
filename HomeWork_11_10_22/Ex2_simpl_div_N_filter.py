# Ex2_sum_num_real_filter. Найти сумму цифр вещественного числа.
str_r = "100.00087"
sum_num_real = sum([int(str_r[i]) for i in range(len(str_r)) if str_r[i] not in {',','.'}])         
print(f'{str_r} ---> сумма цифр этого числа равна {sum_num_real}')