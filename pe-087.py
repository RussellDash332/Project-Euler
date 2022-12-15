from check_primes import sieve

primes = sieve(10**4)[1]

K = 5e7
v = set()
for p in primes:
    s = p**4
    if s >= K: break
    else:
        for q in primes:
            t = s + q**3
            if t >= K: break
            else:
                for r in primes:
                    u = t + r**2
                    if u >= K: break
                    else: v.add(u)
print(len(v))