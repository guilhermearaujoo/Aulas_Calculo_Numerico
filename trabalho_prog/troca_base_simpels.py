def any_to_decimal(num_original, base_original):

    if base_original==10:
        return num_original

    assert(base_original>=2 and base_original<=32), "A base deve ser um número inteiro entre 2 e 32"
    assert(type(num_original)==str), "O número deve ser passado em formato de string"
    assert(type(base_original)==int), "Operação inválida, a base original deve ser do tipo inteiro."

    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    dec = 0
    dec_temp = list(num_original)
    dec_temp.reverse()
    for x,i in enumerate(dec_temp):
        dec += dic.index(i) * base_original**(x)
    return(str(dec))


def decimal_to_any(num_dec, base_final):

    assert(base_final>=2 and base_final<=32), "A base deve ser um número inteiro entre 2 e 32"
    assert(type(num_dec)==str), "O número deve ser passado em formato de string"
    assert(type(base_final)==int), "Operação inválida, a base original deve ser do tipo inteiro."

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


def succ(a, S):

    assert(a>=2 and a<=32), "A base deve ser um número inteiro entre 2 e 32"
    assert(type(a)==int), "A base deve ser um número inteiro"
    assert(type(S)==str), "O número deve ser passado em formato de string"

    S_temp = any_to_decimal(S, a)
    S = str(int(S_temp) + 1)

    return decimal_to_any(S, a)


def ante(a, S):
    assert(a>=2 and a<=32), "A base deve ser um número inteiro entre 2 e 32"
    assert(type(a)==int), "A base deve ser um número inteiro"
    assert(type(S)==str), "O número deve ser passado em formato de string"

    S_temp = any_to_decimal(S, a)
    S = str(int(S_temp) - 1)

    return decimal_to_any(S, a)


def soma(a,S,T):
    assert(a>=2 and a<=32), "A base deve ser um número inteiro entre 2 e 32"
    #não consigo verificar se os numeros possuem a mesma base aqui nesse exemplo
    assert(type(a)==int), "A base deve ser um número inteiro"
    assert(type(S)==str), "O número deve ser passado em formato de string"
    assert(type(T)==str), "O número deve ser passado em formato de string"

    S_temp = any_to_decimal(S, a)
    T_temp = any_to_decimal(T, a)

    soma_temp = int(S_temp) + int(T_temp)

    return decimal_to_any(str(soma_temp), a)


def prod(a,S,T):
    assert(a>=2 and a<=32), "A base deve ser um número inteiro entre 2 e 32"
    #não consigo verificar se os numeros possuem a mesma base aqui nesse exemplo
    assert(type(a)==int), "A base deve ser um número inteiro"
    assert(type(S)==str), "O número deve ser passado em formato de string"
    assert(type(T)==str), "O número deve ser passado em formato de string"

    S_temp = any_to_decimal(S, a)
    T_temp = any_to_decimal(T, a)

    soma_temp = int(S_temp) * int(T_temp)

    return decimal_to_any(str(soma_temp), a)


## para numeros negativos tbm n consigo

a = '2'
b = '3'

print(prod(10, a, b))

