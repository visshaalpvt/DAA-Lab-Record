import heapq

def max_probability(n, edges, succ, start, end):
    g = [[] for _ in range(n)]
    for (a, b), p in zip(edges, succ):
        g[a].append((b, p))
        g[b].append((a, p))
    best = [0.0] * n
    best[start] = 1.0
    pq = [(-1.0, start)]
    while pq:
        p, u = heapq.heappop(pq)
        p = -p
        if u == end:
            return p
        if p < best[u]:
            continue
        for v, w in g[u]:
            if p * w > best[v]:
                best[v] = p * w
                heapq.heappush(pq, (-best[v], v))
    return 0.0

E = [[0, 1], [1, 2], [0, 2]]
print("succProb=[0.5,0.5,0.2] ->", f"{max_probability(3, E, [0.5, 0.5, 0.2], 0, 2):.5f}")
print("succProb=[0.5,0.5,0.3] ->", f"{max_probability(3, E, [0.5, 0.5, 0.3], 0, 2):.5f}")
