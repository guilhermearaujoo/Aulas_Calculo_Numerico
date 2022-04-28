import random

def prob(A, V, N, k, t=10E5):
    
    """
    Esse programa calcula a probabilidade de ter
    'k' bolas vermelhas dentro de uma amostra 
    'N' de bolas, sabendo que o espaço amostral 
    de bolas azuis e vermelhas é de 'V' + 'A'
    
    Parâmetros:
        A (int): número de bolas azuis.
        V (int): número de bolas vermelhas.
        N (int): amostra retirada.
        k (int): número esperado de bolas vermelhas.
        t (int) = opcional: quantidade de vezes que o
                            evento deve ser repetido.
                            
        
    Return:
        A probabilidade do evento 'k' ocorrer
        em uma amostra 'N' em 't' vezes.
    """
    
    times = t
    count = 0
    
    while(times > 0):
        num_A = list("A"*A)
        num_V = list("V"*V)
        num_k = list("V"*k)
        
        total = num_A + num_V
        random.shuffle(total)
        choices = []
        
        for i in range(N):
            x = random.randint(0, len(total)-1)
            if(total[x] == 'V'):
                choices.append(total[x])
                
        if(choices == num_k):
            count += 1
            
        times -= 1
        
    return count/t

