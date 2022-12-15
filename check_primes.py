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
    s = [True] * (n + 1)
    primes = []

    p = 2
    while p <= n:
        if s[p]:
            primes.append(p)
            for i in range(2*p, n, p):
                s[i] = False
        if p == 2:
            p -= 1
        p += 2
    return s, primes