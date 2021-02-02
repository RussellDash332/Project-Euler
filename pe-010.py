from check_primes import is_prime

n = 1
answer = 2 # counted 2 as a prime number so we can skip it
while n < 2_000_000:
    if is_prime(n):
        answer += n
    n += 2
print(answer)