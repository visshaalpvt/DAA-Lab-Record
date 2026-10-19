def subset_sums(items):
    sums = [0]
    for x in items:
        sums += [s + x for s in sums]
    return sums

def subset_sum_exists(arr, target):
    half = len(arr) // 2
    left = subset_sums(arr[:half])
    right = set(subset_sums(arr[half:]))
    return any(target - s in right for s in left)

for arr, t in (([1, 3, 9, 2, 7, 12], 15), ([3, 34, 4, 12, 5, 2], 15), ([2, 4, 6], 5)):
    print(f"E={arr}, exact sum={t} -> {subset_sum_exists(arr, t)}")
