from check_primes import sieve

is_prime, primes = sieve(5*10**7)
rev = []
for p in primes:
    p1 = p**2
    p2 = int(str(p1)[::-1])
    q = int(p2**0.5)
    if p1 != p2 and q**2 == p2 and is_prime[q]:
        rev.append(p1)
assert len(rev) >= 50
print(sum(rev[:50]))