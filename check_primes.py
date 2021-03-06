import math

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def is_composite(n):
    return not is_prime(n)

def sieve(n):
    return list(filter(is_prime,range(1,n)))