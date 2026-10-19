import heapq

def network_delay_time(times, n, k):
    g = [[] for _ in range(n + 1)]
    for u, v, w in times:
        g[u].append((v, w))
    dist = {}
    pq = [(0, k)]
    while pq:
        d, u = heapq.heappop(pq)
        if u in dist:
            continue
        dist[u] = d
        for v, w in g[u]:
            if v not in dist:
                heapq.heappush(pq, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1

print("Example 1 ->", network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print("Example 2 ->", network_delay_time([[1, 2, 1]], 2, 1))
print("Example 3 ->", network_delay_time([[1, 2, 1]], 2, 2))
