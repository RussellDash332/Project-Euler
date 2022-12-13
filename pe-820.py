def modpow(b, m):
    if b == 0:
        return 1
    elif b % 2:
        return 10 * modpow(b-1, m) % m
    r = modpow(b//2, m)
    return r * r % m

def s(n):
    return sum(modpow(n-1, i) * 10 // i % 10 for i in range(1, n+1))

print(s(10**7))