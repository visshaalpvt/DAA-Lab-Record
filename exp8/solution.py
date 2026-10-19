def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

for a in ([64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8]):
    print("Input :", a)
    print("Sorted:", bubble_sort(a))
