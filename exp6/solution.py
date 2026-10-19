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

def max_after_sort(a):
    if not a:
        return None
    return merge_sort(a)[-1]

for a in ([], [5], [3, 3, 3, 3, 3], [9, 2, 7, 4]):
    res = max_after_sort(a)
    print("Input :", a)
    print("Output:", res if res is not None else "None (the list is empty)")
