INF = float("inf")

def dijkstra(graph, src):
    n = len(graph)
    dist, done = [INF] * n, [False] * n
    dist[src] = 0
    for _ in range(n):
        u = min((i for i in range(n) if not done[i]), key=lambda i: dist[i])
        if dist[u] == INF:
            break
        done[u] = True
        for v in range(n):
            if graph[u][v] != INF and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    return dist

g1 = [[0, 10, 3, INF, INF], [INF, 0, 1, 2, INF], [INF, 4, 0, 8, 2], [INF, INF, INF, 0, 7], [INF, INF, INF, 9, 0]]
g2 = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
print("Test Case 1:", dijkstra(g1, 0))
print("Test Case 2:", dijkstra(g2, 0))
