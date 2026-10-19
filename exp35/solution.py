def partition(a, lo, hi):
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

for a in ([10, 16, 8, 12, 15, 6, 3, 9, 5], [12, 4, 78, 23, 45, 67, 89, 1], [38, 27, 43, 3, 9, 82, 10]):
    print("Input :", a)
    quick_sort(a, 0, len(a) - 1)
    print("Output:", ",".join(map(str, a)), "\n")
