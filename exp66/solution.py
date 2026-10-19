from collections import Counter

def num_identical_pairs(nums):
    return sum(c * (c - 1) // 2 for c in Counter(nums).values())

for nums in ([1, 2, 3, 1, 1, 3], [1, 1, 1, 1], [1, 2, 3]):
    print(f"nums={nums} -> {num_identical_pairs(nums)}")
