m = []
for l in open('resources/p083_matrix.txt', 'r').readlines():
    m.append(list(map(int, l.split(','))))

from heapq import *

g = {i: {} for i in range(len(m)*len(m[0]) + 1)}
s, t = 0, len(g) - 1

for r in range(len(m)):
    for c in range(len(m[0])):
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= r+dr < len(m) and 0 <= c+dc < len(m[0]):
                g[r*len(m[0])+c][(r+dr)*len(m[0])+(c+dc)] = m[r][c]
g[t-1][t] = m[-1][-1]

def dijkstra(D, s):
    D[s] = 0
    pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn in g[vv]:
                if nn not in D or D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))

D = {}
dijkstra(D, s)
if t not in D:  print(-1)
else:           print(D[t])