from number_theory import gcd
from check_primes import is_prime

q = 10**6
totient = lambda x: len(list(filter(lambda y: gcd(x,y) == 1, range(1,x))))

"""
ans = 0
n_ans = 0
for n in range(2,q+1):
    totient_value = totient(n)
    if n/totient_value > ans:
        ans = n/totient_value
        n_ans = n
"""

# You can run the above if you want, might take a lot of time.
# But think about this, what if we want to minimize totient(n)?
# Then we must as many prime factors as possible!
# So it's simply 2 x 3 x 5 x 7 x ... until it's still less then 1 million.

p = 0
result = 1
while result <= q:
    if is_prime(p):
        if result*p <= q:
            result *= p
        else:
            break
    p += 1
print(result)