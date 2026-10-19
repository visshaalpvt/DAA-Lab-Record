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

names = list("ABCDEF")
R = [(0, 1, 1), (0, 2, 5), (1, 2, 2), (1, 3, 1), (2, 4, 3), (3, 4, 1), (3, 5, 6), (4, 5, 2)]

b, d, nxt = floyd(6, R)
show(d, "Distance matrix (all links up):", names)
p = path(nxt, 0, 5)
print("Router A to Router F BEFORE failure =", d[0][5], "via", " -> ".join(names[i] for i in p))

R2 = [e for e in R if (e[0], e[1]) != (1, 3)]
b2, d2, nxt2 = floyd(6, R2)
show(d2, "\nDistance matrix (link B-D failed):", names)
p2 = path(nxt2, 0, 5)
print("Router A to Router F AFTER failure  =", d2[0][5], "via", " -> ".join(names[i] for i in p2))
