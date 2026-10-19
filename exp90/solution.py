def permute_unique(nums):
    nums = sorted(nums)
    res, used, cur = [], [False] * len(nums), []
    def bt():
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            cur.append(nums[i])
            bt()
            cur.pop()
            used[i] = False
    bt()
    return res

for nums in ([1, 1, 2], [1, 2, 3]):
    print(f"nums={nums} -> {permute_unique(nums)}")
