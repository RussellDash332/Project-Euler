def ps(n):
    if n == 0:
        return [[]]
    p = ps(n-1)
    return p + [q + [n] for q in p]

psd = {i: ps(i) for i in range(13)}
for i in psd:
    psd[i] = [[(a, b) for a, b in zip([0] + p, p + [i+1])] for p in psd[i]][::-1]

def s(n):
    if n % 9 > 1: return 0
    if n < 4: return 0
    ss = str(n**2)
    for sb in psd[len(ss)-1]:
        if sum(int(ss[a:b]) for a, b in sb) == n:
            return n**2
    return 0

mem = {}
def S(n):
    if n % 9 > 1: return 0
    def helper(n, m):
        if (n, m) in mem: return mem[(n, m)]
        if m < n: return 0
        if n == m:
            mem[(n, m)] = m
            return m
        t = 10
        while t < m:
            q, r = m // t, m % t
            if r < n and helper(n - r, q):
                mem[(n, m)] = m
                return m
            t *= 10
        mem[(n, m)] = 0
        return 0
    return helper(n, n**2)

ss = list(filter(lambda x: x, map(S, range(2, 10**6+1))))
print(sum(ss))