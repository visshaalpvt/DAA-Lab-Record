def unique(a):
    seen, out = set(), []
    for x in a:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

for a in ([3, 7, 3, 5, 2, 5, 9, 2], [-1, 2, -1, 3, 2, -2], [1000000, 999999, 1000000]):
    print("Input :", a)
    print("Output:", unique(a))
