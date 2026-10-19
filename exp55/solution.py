from functools import lru_cache

D = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}

def segmentations(s):
    @lru_cache(None)
    def go(i):
        if i == len(s):
            return [[]]
        res = []
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in D:
                res += [[s[i:j]] + rest for rest in go(j)]
        return res
    return [" ".join(x) for x in go(0)]

for s in ("ilike", "ilikesamsung", "ilikemangoicecream", "iloveyou"):
    segs = segmentations(s)
    print(f"Input: {s}")
    print("Output:", "Yes" if segs else "No")
    for x in segs:
        print(f'   The string can be segmented as "{x}"')
