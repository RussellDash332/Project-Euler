LIMIT = 10**4
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

def num_sum_prime(n):
    mem = {}
    def helper(k, s):
        if (k, s) in mem:
            return mem[(k, s)]
        if k == 0:
            return 1
        elif k < 0 or primes[s] >= n:
            return 0
        else:
            mem[(k, s)] = helper(k, s + 1) + helper(k - primes[s], s)
            return mem[(k, s)]
    return helper(n, 0)

n = 4
while num_sum_prime(n) <= 5000:
    n += 1
print(n)