def rob_line(a):
    prev2 = prev = 0
    for x in a:
        prev2, prev = prev, max(prev, prev2 + x)
    return prev

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_line(nums[:-1]), rob_line(nums[1:]))

for nums in ([2, 3, 2], [1, 2, 3, 1]):
    print(f"nums = {nums}")
    print("The maximum money you can rob without alerting the police is", rob(nums))
