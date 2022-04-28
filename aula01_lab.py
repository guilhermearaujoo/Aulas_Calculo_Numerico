def pot(x,n):
    if(n==0):
        return 1
    else:
       return x*pot(x, n-1)

def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)

def binom(n,m):
    return fact(n)/fact(m)