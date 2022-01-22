import math

def is_prime(n):
    if n < 2:
        return False
    
    raiz = int(math.sqrt(n))+1

    for i in range(2, raiz):
        if n % i == 0:
            return False
    return True
    

def sum_primes(final):

    primos = []

    for n in range(final):
        contador = 0
        for i in range(1, n+1):
            if n % i == 0:
                contador += 1
        if contador == 2:
            #if sum(primos) <= final:
                primos.append(n)
    if sum(primos) == 2:
        primos = [0]

    return sum(primos)
