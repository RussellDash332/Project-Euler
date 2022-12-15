from number_theory import gcd
from check_primes import *

totient = lambda x: len(list(filter(lambda y: gcd(x,y) == 1, range(1,x))))

"""
def check(x):
    ret = sorted(str(totient(x))) == sorted(str(x))
    try:
        q = x/totient(x)
    except:
        q = "nan"
    if ret:
        print(x, ret, q)
    return ret

lst = list(filter(check, range(1, int(1e7) + 1)))
print(min(lst, key=lambda x: x/totient(x)))
"""

p = sieve(5000)[1]
for i in range(len(p)):
    for j in range(i + 1, len(p)):
        if p[i] * p[j] <= 1e7 and sorted(str(p[i] * p[j])) == sorted(str(p[i] * p[j] - p[i] - p[j] + 1)):
            print(p[i] * p[j], p[i] * p[j]/(p[i] * p[j] - p[i] - p[j] + 1))