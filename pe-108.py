from check_primes import sieve
from math import log
from heapq import *

sie, primes = sieve(2*10**5)
rev = dict(map(reversed, enumerate(primes)))

# Smallest n such that the number of solution exceeds D
def f(D):
    # (log_n, s, pf_n)
    MIN_D = 2*D-1
    facs = [(log(2), 3, [(2, 1)])]
    hs = {log(2)}
    while True:
        lg, s, pf = heappop(facs)
        if s > MIN_D:
            f = 1
            for k, v in pf: f *= k**v
            return f
        new_p = primes[rev[pf[-1][0]]+1]
        lgn = round(lg + log(new_p), 12)
        if lgn not in hs:
            hs.add(lgn)
            heappush(facs, (lgn, s*3, pf + [(new_p, 1)]))
        for i, (p, k) in enumerate(pf):
            pf2 = pf.copy()
            pf2[i] = (p, k+1)
            lg2 = round(lg + log(p), 12)
            if lg2 not in hs:
                hs.add(lg2)
                heappush(facs, (lg2, s*(2*k+3)//(2*k+1), pf2))

print(f(1000))