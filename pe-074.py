from math import factorial

f = {i: factorial(i) for i in range(10)}

def df(n):
    return sum(f[int(i)] for i in str(n))

g = {}
def trav(n):
    if n in g: return
    g[n] = df(n)
    trav(g[n])
for i in range(10**6):
    trav(i)

def cyc(n):
    c = set()
    curr = n
    while curr not in c:
        c.add(curr)
        curr = g[curr]
    return len(c)

sixty = []
for i in range(10**6):
    if cyc(i) == 60:
        sixty.append(i)
print(len(sixty))