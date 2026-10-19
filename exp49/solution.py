def schedule(times, transfer):
    L, S = len(times), len(times[0])
    dp = [[0] * L for _ in range(S)]
    par = [[-1] * L for _ in range(S)]
    for l in range(L):
        dp[0][l] = times[l][0]
    for s in range(1, S):
        for l in range(L):
            cost, p = min((dp[s - 1][p] + transfer[p][l], p) for p in range(L))
            dp[s][l] = times[l][s] + cost
            par[s][l] = p
    last = min(range(L), key=lambda l: dp[S - 1][l])
    best, route, l = dp[S - 1][last], [], last
    for s in range(S - 1, -1, -1):
        route.append(l + 1)
        l = par[s][l]
    return best, route[::-1]

times = [[5, 9, 3], [6, 8, 4], [7, 6, 5]]
transfer = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]
best, route = schedule(times, transfer)
print("Minimum total production time:", best)
print("Line used for stations 1..3 :", route)
