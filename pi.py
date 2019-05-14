import math

def pi(nmax):
    a = 2.0
    for n in range(1, nmax):
        a = a * (n*n)/(n*n - 0.25)
    return a

for n in range(7):
    nmax = 10**n
    print (nmax, pi(nmax), math.pi - pi(nmax))





