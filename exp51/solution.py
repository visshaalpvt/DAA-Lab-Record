from itertools import combinations

def held_karp(d):
    n = len(d)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (d[0][k], 0)
    for size in range(2, n):
        for sub in combinations(range(1, n), size):
            bits = sum(1 << b for b in sub)
            for k in sub:
                prev = bits & ~(1 << k)
                C[(bits, k)] = min((C[(prev, m)][0] + d[m][k], m) for m in sub if m != k)
    bits = (1 << n) - 2
    res, last = min((C[(bits, k)][0] + d[k][0], k) for k in range(1, n))
    route = []
    while bits:
        route.append(last)
        bits, last = bits & ~(1 << last), C[(bits, last)][1]
    return res, [0] + route[::-1] + [0]

names = "ABCDE"
dist = {("A","B"):10, ("A","C"):15, ("A","D"):20, ("A","E"):25, ("B","C"):35,
        ("B","D"):25, ("B","E"):30, ("C","D"):30, ("C","E"):20, ("D","E"):15}
def matrix(n):
    m = [[0] * n for _ in range(n)]
    for (a, b), w in dist.items():
        i, j = names.index(a), names.index(b)
        if i < n and j < n:
            m[i][j] = m[j][i] = w
    return m

for n in (4, 5):
    cost, route = held_karp(matrix(n))
    print(f"{n} cities ({names[:n]}): shortest route {' -> '.join(names[i] for i in route)}  total distance = {cost}")
