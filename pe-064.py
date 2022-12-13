from number_theory import gcd

def per(n):
    s = n**0.5
    # rem = (s+a)/b = ir + (s+a-b*ir)/b
    # b/(s+a-b*ir) = (s-a+b*ir)/[(n-(a-b*ir)**2)/b]
    a, b = 0, 1
    alist = []
    MAX_PER = max(100, 10*int(s))
    for _ in range(MAX_PER):
        alist.append((s+a)//b)
        tmp = a-b*alist[-1]
        a, b = -tmp, (n-tmp**2)//b
    pers = []
    alist = alist[1:]
    for d in range(1, MAX_PER//2):
        seqs = set()
        for i in range(len(alist)//d):
            seqs.add(tuple(alist[i*d:(i+1)*d]))
            if len(set(seqs)) != 1: break
        if len(set(seqs)) == 1: pers.append(d)
    res = pers[0]
    for p in pers[1:]:
        res = gcd(res, p)
    return res

MAX = 100
vals = set(range(MAX**2))
sqs = set(map(lambda x: x**2, range(MAX+1)))
vals -= sqs
print(sum([per(i) % 2 for i in sorted(vals)]))