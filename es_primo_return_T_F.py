import math

def is_prime(n):
    if n < 2:
        return False
    
    raiz = int(math.sqrt(n))+1

    for i in range(2, raiz):
        if n % i == 0:
            return False
    return True
