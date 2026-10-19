def solve(n):
    sols, cols, d1, d2, place = [], set(), set(), set(), []
    def bt(r):
        if r == n:
            sols.append(place[:])
            return
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c); place.append(c)
            bt(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c); place.pop()
    bt(0)
    return sols

def draw(sol):
    for c in sol:
        print(" ".join("Q" if j == c else "." for j in range(len(sol))))

for n, how_many in ((4, 2), (5, 2), (8, 2)):
    sols = solve(n)
    print(f"=== N = {n}: {len(sols)} solutions in total, showing {how_many} ===")
    for k in range(how_many):
        print(f"Solution {k + 1}: columns {[c + 1 for c in sols[k]]}")
        draw(sols[k])
        print()
