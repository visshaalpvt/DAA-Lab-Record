def combination_sum2(cands, target):
    cands = sorted(cands)
    res = []
    def bt(start, cur, rem):
        if rem == 0:
            res.append(cur[:])
            return
        for i in range(start, len(cands)):
            if i > start and cands[i] == cands[i - 1]:
                continue
            if cands[i] > rem:
                break
            cur.append(cands[i])
            bt(i + 1, cur, rem - cands[i])
            cur.pop()
    bt(0, [], target)
    return res

print("[10,1,2,7,6,1,5], 8 ->", combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
print("[2,5,2,1,2], 5      ->", combination_sum2([2, 5, 2, 1, 2], 5))
