from check_primes import sieve

primes = sieve(10**4)[1]

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