# Ex4: Реализуйте RLE алгоритм: реализуйте модeль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Входные данные:
# Выходные данные:

def rle_cod(string_in):
	str1 = string_in
	str_cod_out = ''
    count = 1
	while data != '':
		for i in range(1, len(str1)):
			if str1[i] == str1[i - 1]:
				count += 1
			else:
				str_cod_in += str(count) + ' ' + str1[i] + ' '
                count = 1
        if count > 1 or (txt[len(txt)-2] != txt[-1]):
			str_cod_in += str(count) + ' ' + str1[i] + ' '
   		str1 = str1[count:]
	print(str_cod_out)
	return str_cod_out

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res
 
 
 
 
 
 
 
def rle_decod(string_in):
	list_string_in = string_in.split(' ')
	str_decod = ''
	while i < range(len(string_in)):
		if list_string_in[i] != '00':
				count += 1[i] == elem:
				count += 1
		

elem = data[0]
		count = 1
		for i in range(1, len(data)):
			if data[i] == elem:
				count += 1
			else:
				str_cod_in += str(count) + ' ' + elem + ' '
		data = data[count:]
	return str_cod_out

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# test_new = input('Введите данные для сжатия: ')
# with open('file_1.txt', 'w') as f1:
#     f1.write(test_new)


# with open('file_1.txt', 'r') as f1:
#     str1 = f1.read()
# print(str1)


# test_new = input('Введите данные для сжатия: ')
# print(f'Результат сжатия: {coding(s)}')
# print(f'Восстановленные данные: {decoding(coding(s))}')