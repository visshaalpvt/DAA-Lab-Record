count = 0

def merge_sort(a):
    global count
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    l, r = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        count += 1
        if l[i] <= r[j]:
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    return out + l[i:] + r[j:]

for a in ([12, 4, 78, 23, 45, 67, 89, 1], [38, 27, 43, 3, 9, 82, 10]):
    count = 0
    res = merge_sort(a)
    print("Input :", a)
    print("Output:", ",".join(map(str, res)), "| Comparisons =", count)
