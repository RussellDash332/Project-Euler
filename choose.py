def binom(n,r):
    ans = 1
    for i in range(n,n-r,-1):
        ans *= i
    for i in range(1,r+1):
        ans //= i
    return ans