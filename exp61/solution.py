def obst(keys, freq):
    n = len(keys)
    cost = [[0] * (n + 2) for _ in range(n + 2)]
    root = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        cost[i][i], root[i][i] = freq[i - 1], i
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            s = sum(freq[i - 1:j])
            cost[i][j] = float("inf")
            for r in range(i, j + 1):
                c = cost[i][r - 1] + cost[r + 1][j] + s
                if c < cost[i][j]:
                    cost[i][j], root[i][j] = c, r
    return cost, root

def show_tree(keys, root, i, j, indent=0):
    if i > j:
        return
    r = root[i][j]
    print(" " * indent + str(keys[r - 1]))
    show_tree(keys, root, i, r - 1, indent + 4)
    show_tree(keys, root, r + 1, j, indent + 4)

def report(keys, freq):
    n = len(keys)
    cost, root = obst(keys, freq)
    print(f"Keys={keys}, Frequencies={freq}")
    print("Cost table (row i, column j = cost of keys i..j):")
    for i in range(1, n + 1):
        print("  " + " ".join(f"{round(cost[i][j], 2) if j >= i else '-':>6}" for j in range(1, n + 1)))
    print("Root table:")
    for i in range(1, n + 1):
        print("  " + " ".join(f"{root[i][j] if j >= i else '-':>6}" for j in range(1, n + 1)))
    print("Optimal BST (root at top, children indented):")
    show_tree(keys, root, 1, n)
    print("Optimal cost =", round(cost[1][n], 2), "\n")

report(["A", "B", "C", "D"], [0.1, 0.2, 0.4, 0.3])
report([10, 12], [34, 50])
report([10, 12, 20], [34, 8, 50])
