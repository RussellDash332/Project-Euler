from check_primes import is_prime

count = 1 # counted 2 as a prime number so we can skip it
n = 1
while count < 10001: # we need 10000 more
    n += 2
    if is_prime(n):
        count += 1
print(n)