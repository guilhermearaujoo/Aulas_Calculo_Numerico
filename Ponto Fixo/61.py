#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 07:43:10 2022

@author: luiz.cordeiro
"""
import time

def banach(f,x0=0,tempo_max=10,iter_max=1.0e6,explo=None,tol=1.0e-14):
    tempo_inicial=time.time();
    
    if explo==None:
        diverge=abs(1.0e6*x0)
    else:
        diverge=explo
    #end if-else
    
    num_iter=0
    x=x0
    while ((time.time()-tempo_inicial<tempo_max) &
        (num_iter<iter_max) & (abs(x)<diverge)
        & (abs(x-f(x))>0.8*tol*abs(x))):
        x=f(x)
        num_iter+=1
    #end while
    
    print(num_iter)
    #print(x)
    if abs(x-f(x))<tol*abs(x):
        return x
    else:
        return None
    #end if-else#
#end def
    
#def  g(x):
    #return 6/x
#end def
    
x0=1

#y=banach(g,x0)

#print(y)###O valor esperado é "None"

def h(x):
    return (-1/(6+1))+(1/(x*x+1))+x
#end def
    


y=banach(h,x0)

print(y) ##O valor esperado é sqrt(6)