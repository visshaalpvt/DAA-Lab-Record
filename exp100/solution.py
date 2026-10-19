import random
from itertools import combinations

def greedy(U, S):
    U = set(U)
    chosen = []
    while U:
        best = max(S, key=lambda s: len(U & s))
        chosen.append(best)
        U -= best
    return chosen

def optimal(U, S):
    for k in range(1, len(S) + 1):
        for c in combinations(S, k):
            if set().union(*c) >= set(U):
                return list(c)

U = {1, 2, 3, 4, 5, 6, 7}
S = [{1, 2, 3}, {2, 4}, {3, 4, 5, 6}, {4, 5}, {5, 6, 7}, {6, 7}]
g, o = greedy(U, S), optimal(U, S)
print("Greedy Set Cover :", g, "->", len(g), "sets")
print("Optimal Set Cover:", o, "->", len(o), "sets")

print("\nPerformance on random instances:")
random.seed(1)
for size in (8, 12, 16):
    univ = set(range(size))
    sets = [set(random.sample(sorted(univ), random.randint(2, size // 2))) for _ in range(12)]
    sets.append(univ - set().union(*sets))
    sets = [s for s in sets if s]
    print(f"  |U|={size:>2}, |S|={len(sets):>2}: greedy uses {len(greedy(univ, sets))} sets, optimal uses {len(optimal(univ, sets))} sets")
