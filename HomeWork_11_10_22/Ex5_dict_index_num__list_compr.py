# Ex5_dict_index_num_list_compr
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число: "))
print(dictioner_index = {i: 3 * i + 1 for i in range(1, n+1)})