from bisect import bisect_left

def subset_sums(items):
    sums = [(0, [])]
    for x in items:
        sums += [(s + x, sub + [x]) for s, sub in sums]
    return sums

def closest_subset(arr, target):
    half = len(arr) // 2
    L, R = subset_sums(arr[:half]), subset_sums(arr[half:])
    R.sort(key=lambda t: t[0])
    Rs = [t[0] for t in R]
    best = None
    for s, sub in L:
        p = bisect_left(Rs, target - s)
        for q in (p - 1, p):
            if 0 <= q < len(R):
                tot = s + R[q][0]
                if best is None or abs(tot - target) < abs(best[0] - target):
                    best = (tot, sub + R[q][1])
    return best

for arr, t in (([45, 34, 4, 12, 5, 2], 42), ([1, 3, 2, 7, 4, 6], 10)):
    tot, sub = closest_subset(arr, t)
    print(f"Set={arr}, Target={t}")
    print(f"Output: closest sum = {tot}, subset = {sub}, difference = {abs(tot - t)}")
