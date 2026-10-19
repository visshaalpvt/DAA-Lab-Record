def permute(nums):
    res, used, cur = [], [False] * len(nums), []
    def bt():
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True
                cur.append(x)
                bt()
                cur.pop()
                used[i] = False
    bt()
    return res

for nums in ([1, 2, 3], [0, 1], [1]):
    print(f"nums={nums} -> {permute(nums)}")
