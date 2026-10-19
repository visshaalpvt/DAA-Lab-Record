def median_of_medians(arr, k):          # k is 1-based
    if len(arr) <= 5:
        return sorted(arr)[k - 1]
    groups = [sorted(arr[i:i + 5]) for i in range(0, len(arr), 5)]
    medians = [g[len(g) // 2] for g in groups]
    pivot = median_of_medians(medians, (len(medians) + 1) // 2)
    low = [x for x in arr if x < pivot]
    eq = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    if k <= len(low):
        return median_of_medians(low, k)
    if k <= len(low) + len(eq):
        return pivot
    return median_of_medians(high, k - len(low) - len(eq))

for arr, k in (([12, 3, 5, 7, 19], 2), ([12, 3, 5, 7, 4, 19, 26], 3), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)):
    print(f"arr={arr}, k={k} -> {median_of_medians(arr, k)}")
