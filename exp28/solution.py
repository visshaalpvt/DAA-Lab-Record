import math
from itertools import permutations

def distance(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])

def tsp(cities):
    start, rest = cities[0], cities[1:]
    best_d, best_path = float("inf"), None
    for perm in permutations(rest):
        path = [start] + list(perm) + [start]
        d = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))
        if d < best_d:
            best_d, best_path = d, path
    return best_d, best_path

tests = [[(1, 2), (4, 5), (7, 1), (3, 6)], [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]]
for t, cities in enumerate(tests, 1):
    d, path = tsp(cities)
    print(f"Test Case {t}:")
    print("Shortest Distance:", d)
    print("Shortest Path:", path)
