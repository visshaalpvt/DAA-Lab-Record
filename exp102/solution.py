from itertools import product

V = [1, 2, 3, 4]
W = {(1, 2): 2, (1, 3): 1, (2, 3): 3, (2, 4): 4, (3, 4): 2}

def cut_weight(side):
    return sum(w for (u, v), w in W.items() if side[u] != side[v])

def greedy_cut():
    side = {V[0]: 0}
    for v in V[1:]:
        gain = [0, 0]
        for (a, b), w in W.items():
            other = b if a == v else a if b == v else None
            if other in side:
                gain[1 - side[other]] += w          # putting v on side s cuts edges to the other side
        side[v] = 0 if gain[0] >= gain[1] else 1
    return side

def optimal_cut():
    best, best_side = -1, None
    for bits in product((0, 1), repeat=len(V) - 1):
        side = dict(zip(V, (0,) + bits))
        c = cut_weight(side)
        if c > best:
            best, best_side = c, side
    return best_side

def edges_cut(side):
    return [e for e in W if side[e[0]] != side[e[1]]]

g, o = greedy_cut(), optimal_cut()
print("Greedy Maximum Cut    : Cut =", edges_cut(g), "Weight =", cut_weight(g))
print("Optimal Maximum Cut   : Cut =", edges_cut(o), "Weight =", cut_weight(o))
print(f"Performance Comparison: greedy achieves {100 * cut_weight(g) / cut_weight(o):.0f}% of the optimal weight")
