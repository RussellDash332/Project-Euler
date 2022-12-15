def do(precision):
    def gen(theta):
        b = [int(theta*10**precision)]
        for _ in range(precision):
            r = b[-1]//10**precision
            b.append(r*(10**precision+b[-1]-r*10**precision))
        b = ''.join(map(lambda x: str(x//10**precision), b))
        return int(b[:precision+1])

    x, e = 2, 1
    while e <= precision:
        d2 = list(map(lambda i: abs(x*10**precision + i*10**(precision-e) - gen(x + i*10**-e)), range(10)))
        d = d2.index(min(d2))
        x += (d-0.5)*10**-e
        e += 1
    g = str(gen(x))
    print(g[0] + '.' + g[1:])

do(24)