def find_paths(m, n, N, i, j):
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1
    out = 0
    for _ in range(N):
        nd = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                v = dp[r][c]
                if v:
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            nd[nr][nc] += v
                        else:
                            out += v
        dp = nd
    return out

print("m=2,n=2,N=2,i=0,j=0 ->", find_paths(2, 2, 2, 0, 0))
print("m=1,n=3,N=3,i=0,j=1 ->", find_paths(1, 3, 3, 0, 1))
