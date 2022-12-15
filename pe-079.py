# Leetcode SCS
def scs(A, B):
    def lcs(A, B):
        n, m = len(A), len(B)
        dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:    dp[i + 1][j + 1] = dp[i][j] + A[i]
                else:               dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        return dp[-1][-1]

    res, i, j = "", 0, 0
    for c in lcs(A, B):
        while A[i] != c:
            res += A[i]
            i += 1
        while B[j] != c:
            res += B[j]
            j += 1
        res += c
        i, j = i + 1, j + 1
    return res + A[i:] + B[j:]

p = []
for l in open('resources/p079_keylog.txt', 'r').readlines():
    p.append(l.strip())

import random
ss = set()
while len(ss) != 100:
    random.shuffle(p)
    s = ''
    for t in p:
        s = scs(s, t)
    ss.add(s)
print(min(ss, key=int))