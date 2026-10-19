def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

for m, n in ((3, 7), (3, 2)):
    print(f"m = {m}, n = {n} -> {unique_paths(m, n)}")
