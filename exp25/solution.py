import math

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

def closest_pair(pts):
    best = (float("inf"), None, None)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = dist(pts[i], pts[j])
            if d < best[0]:
                best = (d, pts[i], pts[j])
    return best

pts = [(1, 2), (4, 5), (7, 8), (3, 1)]
d, p, q = closest_pair(pts)
print(f"Closest pair: {p} - {q} Minimum distance: {d}")
