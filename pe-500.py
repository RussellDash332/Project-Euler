from check_primes import sieve
from math import log
from heapq import *

primes = sieve(10**7)[1][:500500]
rev = dict(map(reversed, enumerate(primes)))

def pf(n):
    res = {}
    idx = 0
    while n != 1 and idx < len(primes):
        if n % primes[idx] == 0:
            n //= primes[idx]
            res[primes[idx]] = res.get(primes[idx], 0) + 1
        else:
            idx += 1
    if n != 1:
        is_prime = True
        for p in range(primes[idx - 1], int(n**0.5) + 2):
            if n % p == 0:
                is_prime = False
                res[p] = 1
        if is_prime: res[n] = 1
    return res

def f(n):
    res = [0]*n
    s = 0
    facs = [(log(2), 2, 1)]
    for _ in range(n):
        _, p, k = heappop(facs)
        if res[rev[p]] == 0:
            s += 1
            heappush(facs, (log(primes[s]), primes[s], 1))
        res[rev[p]] = 2*k-1
        heappush(facs, (2*k*log(p), p, 2*k))
    #while not res[-1]: res.pop()
    return res

r = 1
MOD = 500500507
for i, k in enumerate(f(500500)):
    r *= pow(primes[i], k, MOD)
    r %= MOD
print(r)