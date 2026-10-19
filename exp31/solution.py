def min_max(a, lo, hi):
    if lo == hi:
        return a[lo], a[lo]
    if hi == lo + 1:
        return (a[lo], a[hi]) if a[lo] < a[hi] else (a[hi], a[lo])
    mid = (lo + hi) // 2
    mn1, mx1 = min_max(a, lo, mid)
    mn2, mx2 = min_max(a, mid + 1, hi)
    return min(mn1, mn2), max(mx1, mx2)

for a in ([5, 7, 3, 4, 9, 12, 6, 2], [1, 3, 5, 7, 9, 11, 13, 15, 17], [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]):
    mn, mx = min_max(a, 0, len(a) - 1)
    print(f"N={len(a)}, a={a}")
    print(f"Output: Min = {mn}, Max = {mx}")
