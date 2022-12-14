LIMIT = 10**6 + 1
sieve = [True] * (LIMIT + 1)
primes = []

p = 2
while p <= LIMIT:
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False
    if p == 2:
        p -= 1
    p += 2

def pf(n):
    res = set()
    idx = 0
    while n != 1 and idx < len(primes):
        if sieve[n]:
            res.add(n)
            return res
        elif n % primes[idx] == 0:
            n //= primes[idx]
            res.add(primes[idx])
        else:
            idx += 1
    return res

def phi(n):
    if n == 1: return 0
    for k in pf(n):
        n //= k
        n *= k - 1
    return n

r = 0
for i in range(10**6):
    r += phi(i + 1)
print(r)