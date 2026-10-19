from itertools import combinations

def total_value(items, values):
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity

def knapsack(weights, values, capacity):
    best, best_sel = -1, []
    n = len(weights)
    for r in range(n + 1):
        for items in combinations(range(n), r):
            if is_feasible(items, weights, capacity):
                v = total_value(items, values)
                if v > best:
                    best, best_sel = v, list(items)
    return best_sel, best

tests = [([2, 3, 1], [4, 5, 3], 4), ([1, 2, 3, 4], [2, 4, 6, 3], 6)]
for t, (w, v, c) in enumerate(tests, 1):
    sel, val = knapsack(w, v, c)
    print(f"Test Case {t}:")
    print("Optimal Selection:", sel)
    print("Total Value:", val)
