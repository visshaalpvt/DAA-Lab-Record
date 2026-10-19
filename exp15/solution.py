def large_group_positions(s):
    res, i = [], 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and s[j + 1] == s[i]:
            j += 1
        if j - i + 1 >= 3:
            res.append([i, j])
        i = j + 1
    return res

for s in ("abbxxxxzzy", "abc", "abcdddeeeeaabbbcd"):
    print(f's = "{s}" ->', large_group_positions(s))
