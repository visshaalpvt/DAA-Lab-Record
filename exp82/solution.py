def solve(R, C, blocked=lambda r, c: False):
    place = []
    def bt(r):
        if r == R:
            return True
        for c in range(C):
            if blocked(r, c):
                continue
            if any(c == pc or abs(r - pr) == abs(c - pc) for pr, pc in enumerate(place)):
                continue
            place.append(c)
            if bt(r + 1):
                return True
            place.pop()
        return False
    return place[:] if bt(0) else None

def draw(sol, R, C, blocked=lambda r, c: False):
    for r in range(R):
        print(" ".join("Q" if sol[r] == c else ("X" if blocked(r, c) else ".") for c in range(C)))

def run(title, R, C, blocked=lambda r, c: False):
    sol = solve(R, C, blocked)
    print(title)
    if sol is None:
        print("No solution")
    else:
        print("Possible solution (column of the queen in each row, 1-based):", [c + 1 for c in sol])
        draw(sol, R, C, blocked)
    print()

run("a) 8 x 10 board", 8, 10)
obst = {(2, 2), (4, 4)}                                  # 1-based obstacle squares
run("b) 5 x 5 board, obstacles X at (2,2) and (4,4)", 5, 5, lambda r, c: (r + 1, c + 1) in obst)
run("c) 6 x 6 board, first queen restricted from columns 2 and 4", 6, 6, lambda r, c: r == 0 and c + 1 in (2, 4))
