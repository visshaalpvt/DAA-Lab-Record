import math

def colour(n, edges, k):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    col = [0] * n
    def bt(v):
        if v == n:
            return True
        for c in range(1, k + 1):
            if all(col[u] != c for u in adj[v]):
                col[v] = c
                if bt(v + 1):
                    return True
                col[v] = 0
        return False
    return col if bt(0) else None

n, edges, k = 4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)], 3
print("Colouring with k = 3 colours:", colour(n, edges, k))
for m in range(1, n + 1):
    c = colour(n, edges, m)
    if c:
        print(f"Minimum number of colours = {m}, colouring = {c}")
        break
print("Maximum number of regions you can colour:", math.ceil(n / 3))
