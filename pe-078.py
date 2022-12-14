p = [1]
MOD = 10**6
while p[-1] % MOD != 0:
    n = len(p)
    r = 0
    k = 1
    while True:
        g = n - k*(3*k-1)//2
        if g < 0: break
        r += [-1, 1][k % 2] * p[g]
        if k > 0:   k = -k
        else:       k = 1-k
    p.append(r % MOD)
print(len(p) - 1)