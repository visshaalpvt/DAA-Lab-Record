def subsets(a, dedupe=False):
    a = sorted(a)
    res = []
    def bt(start, cur):
        res.append(cur[:])
        for i in range(start, len(a)):
            if dedupe and i > start and a[i] == a[i - 1]:
                continue
            cur.append(a[i])
            bt(i + 1, cur)
            cur.pop()
    bt(0, [])
    return sorted(res, key=lambda s: (len(s), s))

print("Subsets of [1,2,3]:", subsets([1, 2, 3]))
print("[1,2,2] without duplicate handling:", subsets([1, 2, 2]))
print("[1,2,2] with duplicate handling   :", subsets([1, 2, 2], dedupe=True))
