def pot(x,n):
    '''
    Função que calcula a multiplicação entre dois valores.
        Parameters:
            x(int): um inteiro decimal
            n(int): um inteiro decimal
        Returns:
            asw(int): o resultado da multiplicação.
    '''
    asw = x*n
    return asw


print("\nEsse programa deverá calcular o expoente de um número.\n\n")
x = int(input("digite um numero: "))
n = int(input("digite o expoente: "))

res = 0
aux = n
while aux > 0:
    res += pot(x, n)
    aux -= 1

print("\nO resultado de {}^{} é igual à {} \n".format(x, n, res))
