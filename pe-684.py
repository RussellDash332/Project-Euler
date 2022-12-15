from number_theory import fib

MOD = 10**9 + 7

def modpow(a, b, m):
    if b == 0:
        return 1
    elif b % 2:
        return a * modpow(a, b-1, m) % m
    r = modpow(a, b//2, m)
    return r * r % m

def s(n):
    d = []
    for i in range(9, 0, -1):
        while n >= i:
            n -= i
            d.append(i)
    return int(''.join(map(str, reversed(d))))

def S(n):
    excess, full = n % 9, n - n % 9
    mp = modpow(10, full // 9, MOD)
    return (-full + (excess + 6) * (mp - 1) + excess*(excess + 1)//2 * mp) % MOD

print(sum(S(fib(i)) for i in range(2, 91)) % (10**9 + 7))