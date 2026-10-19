def combination_sum(cands, target):
    res = []
    def bt(start, cur, rem):
        if rem == 0:
            res.append(cur[:])
            return
        for i in range(start, len(cands)):
            if cands[i] > rem:
                continue
            cur.append(cands[i])
            bt(i, cur, rem - cands[i])
            cur.pop()
    bt(0, [], target)
    return res

print("[2,3,6,7], 7 ->", combination_sum([2, 3, 6, 7], 7))
print("[2,3,5], 8   ->", combination_sum([2, 3, 5], 8))
