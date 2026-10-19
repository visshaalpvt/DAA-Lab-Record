from itertools import combinations

def approx_vc(E):
    cover = set()
    for u, v in E:
        if u not in cover and v not in cover:
            cover |= {u, v}
    return cover

def exact_vc(V, E):
    for k in range(len(V) + 1):
        for c in combinations(V, k):
            if all(u in c or v in c for u, v in E):
                return set(c)

V, E = [1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
a, e = approx_vc(E), exact_vc(V, E)
print("Approximation Vertex Cover:", sorted(a), "size", len(a))
print("Exact Vertex Cover (Brute-Force):", sorted(e), "size", len(e))
print(f"Performance Comparison: approximation / optimal = {len(a)}/{len(e)} = {len(a) / len(e):.2f} (guaranteed <= 2)")
