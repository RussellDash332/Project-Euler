P = 10**9; ans = 0
for a in range(2, (P+2)//3):
    for h, p in (((3*a-1)*(a+1)*(a-1)**2, 3*a-1), ((3*a+1)*(a-1)*(a+1)**2, 3*a+1)):
        if round(h**0.5)**2 == h and h % 16 == 0:
            ans += p; print(a, h, ans)
print(ans)