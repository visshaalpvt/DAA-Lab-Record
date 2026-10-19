def k_closest(points, k):
    order = sorted(range(len(points)), key=lambda i: points[i][0] ** 2 + points[i][1] ** 2)[:k]
    return [points[i] for i in sorted(order)]

for pts, k in (([[1, 3], [-2, 2], [5, 8], [0, 1]], 2), ([[1, 3], [-2, 2]], 1), ([[3, 3], [5, -1], [-2, 4]], 2)):
    print(f"points={pts}, k={k}")
    print("Output:", k_closest(pts, k))
