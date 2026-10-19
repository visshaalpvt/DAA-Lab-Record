def unique_paths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]

for m, n in ((7, 3), (3, 2)):
    print(f"m = {m}, n = {n} -> {unique_paths(m, n)}")
