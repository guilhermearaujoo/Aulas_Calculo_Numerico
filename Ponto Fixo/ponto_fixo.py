#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: guilherme
"""

import math 

def h(x):
    return (-1/(6+1))+(1/(x*x+1))+x


def ponto_fixo(f, p0, tol, nmax, verbose=False):
    
    """
    Algoritimo do ponto fixo
    
    Recebe:
        f       => função a ser encontrada a raiz
        p0      => Chute inicial
        tol     => tolerância máxima permitida para o erro
        nmax    => número máximo de iterações
        verbose => Mostra passo a passo?
        
    Retorna: 
        n    => Número de iterações
        p    => Raiz de f
        erro => Erro |p_n - p_{n-1}|, erro do passo atual menos o erro do passo anterior
    """
    
    assert tol>0, "Tolerância deve ser maior que 0"
    assert nmax>0, "Numero máximo de iterações deve ser maior que 0"
    
    n=0
    if verbose:
        print("  n           p                erro")
        print(f"{n:3}       {p0:.6e}")
    
    n+=1 
    p_velho = p0
    p_novo = f(p_velho)
    erro = math.fabs(p_novo - p_velho)
    print(f"{n:3}       {p_novo:.6e}        {erro:.3e}")
    
    #duas condições de limite
    while erro>tol and n<nmax:
        n += 1
        p_velho = p_novo
        p_novo = f(p_velho)
        erro = math.fabs(p_novo-p_velho)
        if verbose:
            print(f"{n:3}       {p_novo:.6e}        {erro:.3e}")
            
    return n, p_novo, erro

            
        
            