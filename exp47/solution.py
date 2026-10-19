def dice_throw(sides, dice, target):
    dp = [[0] * (target + 1) for _ in range(dice + 1)]
    dp[0][0] = 1
    for d in range(1, dice + 1):
        for s in range(1, target + 1):
            dp[d][s] = sum(dp[d - 1][s - f] for f in range(1, min(sides, s) + 1))
    return dp[dice][target]

for t, (sides, dice, target) in enumerate(((6, 2, 7), (4, 3, 10)), 1):
    print(f"Test Case {t}:")
    print(f"Number of ways to reach sum {target}: {dice_throw(sides, dice, target)}")
