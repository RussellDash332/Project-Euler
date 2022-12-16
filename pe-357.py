from check_primes import sieve

LIM = 10**8
sie = sieve(LIM + 2)[0]
pg = [1]
for n in range(2, LIM + 1, 4):
    if sie[n + 1] and sie[n//2 + 2]:
        can = True
        for p in range(3, int(n**0.5) + 1):
            if n % p == 0 and not sie[p + n//p]:
                can = False
                break
        if can: pg.append(n)
print(sum(pg))