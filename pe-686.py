from math import log10

def p(L, n):
    pp, m = [], 0
    k = len(str(L)) - 1
    l, u = log10(L) - k, log10(L + 1) - k
    while len(pp) != n:
        ml2 = m*log10(2)
        if l < ml2 - int(ml2) < u:
        #if int(pow(10, ml2 - int(ml2) + k)) == L:
            pp.append(m)
        m += 1
    return pp[-1]

print(p(123, 678910))