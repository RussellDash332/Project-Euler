def modpow(a, b, m):
    if b == 0:
        return 1
    elif b % 2:
        return a * modpow(a, b-1, m) % m
    r = modpow(a, b//2, m)
    return r * r % m
print(28433 * modpow(2, 7830457, 10**10) % 10**10 + 1)