def any_to_decimal(num_original, base_original):

    if base_original==10:
        return num_original

    assert(type(base_original)==int), "Operação inválida, a base original deve ser do tipo inteiro."

    num_original = "1010"
    base_original = 2

    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    dec = 0
    dec_temp = list(num_original)
    dec_temp.reverse()
    for x,i in enumerate(dec_temp):
        dec += dic.index(i) * base_original**(x)
    return(str(dec))


def decimal_to_any(num_dec, base_final):

    assert(type(base_final)==int), "Operação inválida, a base final deve ser do tipo inteiro."
    num_dec = int(num_dec)

    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numero_final_temp = []
    numero_final = ''
    while True:
        
        temp_numero_final = num_dec%base_final
        numero_final_temp.append(temp_numero_final)

        if int(num_dec/base_final) == 0:
            break
        num_dec = int(num_dec/base_final)

    numero_final_temp.reverse()
    for i in numero_final_temp:
        numero_final += dic[i]  
    return numero_final


 
def troca_base(base_original,base_final, num_original):
    num_dec = any_to_decimal(num_original,base_original)
    num_final = decimal_to_any(num_dec,base_final)
    return num_final


print(troca_base(10, 18, '100'))