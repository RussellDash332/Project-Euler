from decimal import *
from functools import *
from math import *
getcontext().prec = 30
def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]) > 1e-16
def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]
def qu(a):
    if a[0] > 0: return 1
    if a[0]==0 and a[1] > 0: return 2
    if a[0] < 0: return 3
    if a[0]==0 and a[1] < 0: return 4
    return 0
def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]
def cmp(a, b):
    return qu(a)-qu(b) or -cross(a, b)
def minkowski(P, Q):
    p = P.index(min(P)); q = Q.index(min(Q)); a = len(P); b = len(Q); R = [(P[p][0]+Q[q][0], P[p][1]+Q[q][1])]; edges = []
    for i in range(a): edges.append((P[(p+i+1)%a][0]-P[(p+i)%a][0], P[(p+i+1)%a][1]-P[(p+i)%a][1]))
    for i in range(b): edges.append((Q[(q+i+1)%b][0]-Q[(q+i)%b][0], Q[(q+i+1)%b][1]-Q[(q+i)%b][1]))
    edges.sort(key=cmp_to_key(cmp))
    for x, y in edges[:-1]: R.append((R[-1][0]+x, R[-1][1]+y))
    return R
def make(n):
    return [(Decimal(cos((2*k-1)/n*pi)), Decimal(sin((2*k-1)/n*pi))) for k in range(1, n+1)]
S = make(1864)
for i in range(1865, 1910): S = minkowski(S, make(i))
print(len(chull(S)))