f = {i: i**2 for i in range(10)}

def df(n):
    return sum(f[int(i)] for i in str(n))

g = {}
def trav(n):
    if n in g: return
    g[n] = df(n)
    trav(g[n])
for i in range(10**7):
    trav(i)

g2 = {}
for n in g:
    if g[n] not in g2:
        g2[g[n]] = []
    g2[g[n]].append(n)

res = set()
def dfs(n):
    if n in res: return
    res.add(n)
    if n in g2:
        for n2 in g2[n]:
            dfs(n2)
dfs(89)
print(len(res))