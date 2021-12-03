matrix = list(map(lambda x:list(map(int,x.strip().split(","))),open("resources/p081_matrix.txt").readlines()))

dp = []
for _ in range(len(matrix)):
    dp.append([0] * len(matrix[0]))

dp[0][0] = matrix[0][0]
for i in range(1, len(matrix)):
    dp[i][0] = dp[i - 1][0] + matrix[i][0]
for i in range(1, len(matrix[0])):
    dp[0][i] = dp[0][i - 1] + matrix[0][i]
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
print(dp[-1][-1])