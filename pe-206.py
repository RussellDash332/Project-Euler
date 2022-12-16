s = []
for i in range(135*107, 14*108):
    if i % 10 != 0: continue
    add = True
    q, f = i**2, 1
    for d in range(9, 0, -1):
        f *= 100
        if q // f % 10 != d:
            add = False
            break
    if add: s.append((i, i**2))
for p in s:
    print(p[0])