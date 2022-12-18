MAXL = 1_500_000
h = {}
for m in range(int((MAXL//2)**0.5+99)):
    for n in range(1, m):
        k = 2
        while True:
            p = k*m*(m+n)
            if p > MAXL: break
            else:
                if p not in h: h[p] = set()
                u, v, w = k//2*(m**2-n**2), k*m*n, k//2*(m**2+n**2)
                if u > v:
                    u, v = v, u
                h[p] |= {(u, v, w)}
            k += 2
sing = 0
for k, v in sorted(h.items()):
    sing += len(v) == 1
print(sing)