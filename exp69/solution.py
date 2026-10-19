def max_coins(piles):
    piles = sorted(piles)
    n = len(piles) // 3
    return sum(piles[n::2])

for p in ([2, 4, 1, 2, 7, 8], [2, 4, 5]):
    print(f"piles = {p} -> {max_coins(p)}")
