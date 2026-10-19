def find_peak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo

for nums in ([1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4]):
    i = find_peak(nums)
    print(f"nums={nums} -> index {i} (value {nums[i]})")
