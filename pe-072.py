from check_primes import sieve
ss, primes = sieve(10**6 + 1)

def pf(n):
    res = set()
    idx = 0
    while n != 1 and idx < len(primes):
        if ss[n]:
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