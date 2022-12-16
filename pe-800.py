from check_primes import sieve
from math import log

s, primes = sieve(3*10**7)
logc = 800800*log(800800)
hybrid = 0

i, j = 0, len(primes)-1
while i < j:
    while j >= 0 and primes[i]*log(primes[j]) + primes[j]*log(primes[i]) > logc:
        j -= 1
    hybrid += j-i
    j += 1
    i += 1
print(hybrid)