def coding(cod_in):
    count = 1
    cod_out = ''
    for i in range(len(cod_in) - 1):
        if cod_in[i] == cod_in[i + 1]:
            count += 1
        else:
            cod_out += str(count) + ' ' + cod_in[i] + ' '
            count = 1
    if count > 1 or (cod_in[-2] != cod_in[-1]):
        cod_out += str(count) + ' ' + cod_in[-1]
    return cod_out

def decoding(cod_in):
    list_cod_in = cod_in.split()
    print(list_cod_in)
    decod_out = ''
    i = 0
    while i <= len(list_cod_in):
        decod_out = decod_out + str(list_cod_in[i + 1])*(int(list_cod_in[i]))
        i += 2
        print(decod_out)
    print(decod_out)
    return decod_out

