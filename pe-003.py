from check_primes import is_prime

# highest prime factor
def hpf(n):
    result = 1 # some small number
    for i in range(n):
        if n % (i+1) == 0 and is_prime(i+1):
            result = i+1
            print(result) # track
    return result

print(hpf(600851475143))