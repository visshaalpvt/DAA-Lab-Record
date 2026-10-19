def bubble_sort(a):
    a = a[:]
    n, passes = len(a), 0
    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, passes

for a in ([64, 25, 12, 22, 11], [29, 10, 14, 37, 13], [3, 5, 2, 1, 4], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]):
    res, p = bubble_sort(a)
    print(f"Input: {a} -> Output: {res}  (passes used: {p})")
