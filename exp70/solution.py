def min_added_coins(coins, target):
    coins = sorted(coins)
    reach, i, added = 0, 0, 0
    while reach < target:
        if i < len(coins) and coins[i] <= reach + 1:
            reach += coins[i]
            i += 1
        else:
            reach += reach + 1
            added += 1
    return added

for coins, t in (([1, 4, 10], 19), ([1, 4, 10, 5, 7, 19], 19)):
    print(f"coins={coins}, target={t} -> {min_added_coins(coins, t)}")
