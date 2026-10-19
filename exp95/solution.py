def power_set(a):
    a = sorted(a)
    res = []
    def bt(start, cur):
        res.append(cur[:])
        for i in range(start, len(a)):
            cur.append(a[i])
            bt(i + 1, cur)
            cur.pop()
    bt(0, [])
    return res

def subsets_with(a, x):
    rest = [v for v in a if v != x]
    return sorted((sorted(s + [x]) for s in power_set(rest)), key=lambda s: (len(s), s))

print("Subsets of [2,3,4,5] containing 3:", subsets_with([2, 3, 4, 5], 3))
print("Power set of [1,2,3]:", power_set([1, 2, 3]))
print("Power set of [0]    :", power_set([0]))
