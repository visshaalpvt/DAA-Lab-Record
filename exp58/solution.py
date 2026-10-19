INF = float("inf")

def floyd(n, edges, directed=False):
    d = [[INF] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        d[u][v] = w; nxt[u][v] = v
        if not directed:
            d[v][u] = w; nxt[v][u] = u
    before = [r[:] for r in d]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]
    return before, d, nxt

def path(nxt, u, v):
    if nxt[u][v] is None:
        return []
    p = [u]
    while u != v:
        u = nxt[u][v]
        p.append(u)
    return p

def show(m, title, names):
    print(title)
    print("      " + " ".join(f"{x:>5}" for x in names))
    for i, row in enumerate(m):
        print(f"{names[i]:>5} " + " ".join(f"{'INF' if v == INF else v:>5}" for v in row))

def find_city(n, edges, thr):
    _, d, _ = floyd(n, edges)
    best, ans = None, -1
    for i in range(n):
        c = sum(1 for j in range(n) if i != j and d[i][j] <= thr)
        if best is None or c <= best:
            best, ans = c, i
    return ans

print("Threshold problem: city =", find_city(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))

print("\n(a) Four cities (directed)")
E = [(0, 1, 3), (0, 2, 8), (0, 3, -4), (1, 3, 1), (1, 2, 4), (2, 0, 2), (3, 2, -5), (3, 1, 6)]
names = ["C1", "C2", "C3", "C4"]
b, d, nxt = floyd(4, E, directed=True)
show(b, "Distance matrix BEFORE:", names)
show(d, "Distance matrix AFTER:", names)
p = path(nxt, 0, 2)
print("Shortest path City 1 to City 3:", " -> ".join(names[i] for i in p), "| distance =", d[0][2])

print("\n(b) Six routers")
names = list("ABCDEF")
R = [(0, 1, 1), (0, 2, 5), (1, 2, 2), (1, 3, 1), (2, 4, 3), (3, 4, 1), (3, 5, 6), (4, 5, 2)]
b, d, nxt = floyd(6, R)
show(b, "Distance matrix BEFORE:", names)
show(d, "Distance matrix AFTER:", names)
p = path(nxt, 0, 5)
print("Shortest path A to F:", " -> ".join(names[i] for i in p), "| distance =", d[0][5])
