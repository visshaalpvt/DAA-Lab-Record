from itertools import permutations

def total_cost(assignment, cost):
    return sum(cost[w][t] for w, t in enumerate(assignment))

def assignment_problem(cost):
    best, best_a = float("inf"), None
    for perm in permutations(range(len(cost))):
        c = total_cost(perm, cost)
        if c < best:
            best, best_a = c, perm
    return best_a, best

tests = [[[3, 10, 7], [8, 5, 12], [4, 6, 9]], [[15, 9, 4], [8, 7, 18], [6, 12, 11]]]
for t, m in enumerate(tests, 1):
    a, c = assignment_problem(m)
    print(f"Test Case {t}:")
    print("Optimal Assignment:", [f"(worker {w + 1}, task {task + 1})" for w, task in enumerate(a)])
    print("Total Cost:", c)
