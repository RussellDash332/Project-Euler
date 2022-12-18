def sqrt(x, prec):
    prec *= 2
    n = 10**prec*x
    lo, hi = 1, n
    while abs(hi - lo) >= 2:
        mid = (lo + hi) // 2
        exp = mid**2
        if exp == n:
            break
        elif exp < n:
            lo = mid
        else:
            hi = mid
    g = str(mid)
    return g

def d(n):
    prec = 120
    s = sqrt(n, prec)
    return sum(map(int, s[:100]))

vals = set(range(101)) - {x**2 for x in range(11)}
print(sum(map(d, vals)))