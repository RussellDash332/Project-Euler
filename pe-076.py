mem = {}
def num_sum(n):
    def helper(k, s):
        if (k, s) in mem:
            return mem[(k, s)]
        if k == 0:
            return 1
        elif k < 0 or s == n:
            return 0
        else:
            mem[(k, s)] = helper(k, s + 1) + helper(k - s, s)
            return mem[(k, s)]
    return helper(n, 1)

# DP approach
def num_sum(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for s in range(n + 1):
        dp[0][s] = 1
    for k in range(1, n + 1):
        for s in range(n - 1, 0, -1):
            if k >= s:  dp[k][s] = dp[k][s + 1] + dp[k - s][s]
            else:       dp[k][s] = dp[k][s + 1]
    return dp[n][1]

print(num_sum(100))