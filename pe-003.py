from check_primes import is_prime

def hpf(n):
    factor = []
    result = 1
    for i in range(n):
        if n % (i+1) == 0:
            factor.append(i+1)
    for i in range(len(factor)):
        if is_prime(factor[i]):
            result = factor[i]
    return result

print(hpf(600851475143))