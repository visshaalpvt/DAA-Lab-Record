def sum_counts(nums):
    n, total = len(nums), 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(nums[j])
            total += len(seen) ** 2
    return total

for nums in ([1, 2, 1], [1, 1]):
    print("nums =", nums, "->", sum_counts(nums))
