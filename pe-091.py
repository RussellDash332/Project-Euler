ans = 0
L = 51
for x1 in range(L):
    for y1 in range(L):
        for x2 in range(L):
            for y2 in range(L):
                aq, bq, cq = x1**2+y1**2, x2**2+y2**2, (x1-x2)**2+(y1-y2)**2
                ans += (aq+bq+cq == 2*max(aq, bq, cq) and min(aq, bq, cq) > 0)
print(ans//2)