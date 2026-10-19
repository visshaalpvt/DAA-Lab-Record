from itertools import permutations

def verify(edges, path, vertices):
    adj = {v: set() for v in vertices}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return sorted(path) == sorted(vertices) and all(path[i + 1] in adj[path[i]] for i in range(len(path) - 1))

def find_path(vertices, edges):
    for p in permutations(vertices):
        if verify(edges, list(p), vertices):
            return list(p)
    return None

V = ["A", "B", "C", "D"]
E = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
p = find_path(V, E)
print("Hamiltonian Path Exists:", p is not None, "" if p is None else f"(Path: {' -> '.join(p)})")
print("Verifier accepts ['A','B','C','D']:", verify(E, ["A", "B", "C", "D"], V))
print("Verifier accepts ['A','C','B','D']:", verify(E, ["A", "C", "B", "D"], V))
