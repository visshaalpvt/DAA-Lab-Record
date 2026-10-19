def find_kth_positive(arr, k):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] - (mid + 1) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo + k

for arr, k in (([2, 3, 4, 7, 11], 5), ([1, 2, 3, 4], 2)):
    print(f"arr={arr}, k={k} -> {find_kth_positive(arr, k)}")
