def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    l, r = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    return out + l[i:] + r[j:]

for a in ([31, 23, 35, 27, 11, 21, 15, 28], [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]):
    print("Input :", a)
    print("Output:", ",".join(map(str, merge_sort(a))))
