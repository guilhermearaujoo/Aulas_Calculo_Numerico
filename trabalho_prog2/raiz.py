# M�todo do ponto  fixo
def ponto_fixo(f, coef, p0, tol, nmax, verbose=False):
    
    """
    Algoritimo do ponto fixo
    
    Recebe:
        f       => fun��o a ser encontrada a raiz
        p0      => Chute inicial
        tol     => tolerancia m�xima permitida para o erro
        nmax    => n�mero m�ximo de itera��es
        verbose => Mostra passo a passo?
        
    Retorna: 
        n    => N�ero de itera��es
        p    => Raiz de f
        erro => Erro |p_n - p_{n-1}|, erro do passo atual menos o erro do passo anterior
    """
    
    assert tol>0, "Tolerancia deve ser maior que 0"
    assert nmax>0, "Numero m�ximo de itera��es deve ser maior que 0"
    
    n=0
    if verbose:
        print("  n           p                erro")
        print(f"{n:3}       {p0:.6e}")
    
    n+=1 
    p_velho = p0
    p_novo = f(coef, p_velho)
    erro = abs(p_novo - p_velho)
    print(f"{n:3}       {p_novo:.6e}        {erro:.3e}")
    
    #duas condições de limite
    while erro>tol and n<nmax:
        n += 1
        p_velho = p_novo
        p_novo = f(coef, p_velho)
        erro = abs(p_novo-p_velho)
        if verbose:
            print(f"{n:3}       {p_novo:.6e}        {erro:.3e}")
            
    return n, p_novo, erro


# escalonamento de matriz
def escalona(A, tol=1.0e-20, verbose=False):
    
    """
    Input:
        A: a amtriz a ser escalonada
        tol: tolerancia num�rica suportada 
        verbose: se TRUE imprime o passo a passso da fun��o
        
    Return:
        A: a matriz A escalonada
    """
    
    n=len(A)
    
    if verbose: print(A)
        
    
    # escalonamento para cada uma das colunas
    for c in range(n-1):
        
        if verbose:
            print("\n\n--------------------")
            print("Elimina��oo Gaussiana na coluna %d." % c, end="\n")
        
        
        #Procuro um Pivô 
        p=c
        while abs(A[p,c])<tol and p<n-1:
            p+=1
            assert(abs(A[p,c])>tol), "O Pivo n�o nulo o algoritimo falha\n"
        
        
        # Se for necess�rio, troca linhas!
        if p==c:
            if verbose:
                print("Pivo A[%d,%d] = %.6g, n�o preciso trocar as linhas\n"
                      % (p, c, A[p,c]))
            else: 
                # o pivo n�o est� na linha atual fa�o uma troca de linhas
                if verbose:
                    print("Pivo A[%d,%d] = %.6g, trocando as linhas %d <=> %d\n"
                          % (p, c, A[p,c], p, c))
                x = -A[c].copy()

                A[c] = A[p]
                A[p] = x
            
            # Faz o escalonamento para coluna c
            if verbose: print('')
            for l in range(c+1, n):
                coef = A[l, c]/ A[c,c]
                if verbose: print("E_%d - %.2f E_%d -> E_%d)" % (l, coef, c, l))
                A[l] = A[l] - coef*A[c] 
            if verbose: print(A, "\n\n")
            
    return A 


# Substitui��o regressiva
def subs_regressiva(A, verbose=False):
    
    n=len(A)
            
    #N�o posso inicar a substitui��o regressiva
 
    #assert(A[n-1, n-1] != 0), "A[%d, %d] = 0, N�o existe solu��o �nica" % (n-1, n-1)
      
        
    #Substitui��o Regressiva
    
    if verbose:
        print("\n\n--------------------")
        print("Substitui��o Regressiva\n")
        
    x = [0]*n
    if(A[n-1, n-1]==0):
        x[n-1] = 0
    else: 
        x[n-1] = A[n-1, n]/A[n-1, n-1]

    
    if verbose:
        print("x_%d = %.6g / %.6g = %.6g" % (n-1, A[n-1, n], A[n-1, n-1], x[n-1]))
    
    
    for i in range(n-2, -1, -1):
        s = 0
        strsoma = ""
        if verbose: print("x_%d = " % (i), end ='')
        for j in range(i+1, n):
            s+= A[i,j]*x[j]
            if verbose: strsoma += "%.6g x_%d + " % (A[i,j], j)
        
        if(A[i,i]==0):
            x[i] = 0
        else:
            x[i] = (A[i,n] - s)/A[i,i]
        
        if verbose: 
            print("(%.6g - (%s) )/ %.6g = %.6g" % (A[i,n], strsoma, A[i,i], x[i]))
        if verbose: print("{} \n".format(x))
        
    return x



# Elimina��o Gaussiana
def eliminacao_guassiana(A, verbose=False):
    """
    Algoritimo de Elimina��o Gaussiana
    
    Recebe:
        A       => Matriz aumentada de coeficientes
        verbode => Imprime passo a passo?
        
    Retorna:
        x       => Vetor solu��oo
    """
    size = A.shape
    assert(size[0] < size[1]), "Matriz inv�lida"
    
    A = escalona(A, 1.0e-10, verbose)
    x = subs_regressiva(A, verbose)
    

    return(x)


    