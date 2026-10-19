from functools import lru_cache

def find_target_sum_ways(nums, target):
    @lru_cache(None)
    def go(i, s):
        if i == len(nums):
            return 1 if s == target else 0
        return go(i + 1, s + nums[i]) + go(i + 1, s - nums[i])
    return go(0, 0)

print("nums=[1,1,1,1,1], target=3 ->", find_target_sum_ways((1, 1, 1, 1, 1), 3))
print("nums=[1], target=1 ->", find_target_sum_ways((1,), 1))
