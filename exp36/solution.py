def partition(a, lo, hi):
    mid = (lo + hi) // 2
    a[lo], a[mid] = a[mid], a[lo]          # middle element becomes the pivot
    pivot, i = a[lo], lo + 1
    for j in range(lo + 1, hi + 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[lo], a[i - 1] = a[i - 1], a[lo]
    return i - 1

def quick_sort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        print(f"pivot={a[p]:>3} (index {p}) a[{lo}..{hi}] -> {a}")
        quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)

for a in ([19, 72, 35, 46, 58, 91, 22, 31], [31, 23, 35, 27, 11, 21, 15, 28], [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]):
    print("Input :", a)
    quick_sort(a, 0, len(a) - 1)
    print("Output:", ",".join(map(str, a)), "\n")
