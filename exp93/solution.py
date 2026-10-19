def hamiltonian_cycle(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    path, used = [0], [False] * n
    used[0] = True
    def bt():
        if len(path) == n:
            return 0 in adj[path[-1]]
        for v in sorted(adj[path[-1]]):
            if not used[v]:
                used[v] = True
                path.append(v)
                if bt():
                    return True
                path.pop()
                used[v] = False
        return False
    return path + [0] if bt() else None

n, edges = 4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
cyc = hamiltonian_cycle(n, edges)
print("Hamiltonian Cycle Exists:", cyc is not None, "" if cyc is None else f"(Example cycle: {' -> '.join(map(str, cyc))})")
