def insertion_sort(a, key=lambda x: x):
    a = a[:]
    for i in range(1, len(a)):
        cur, j = a[i], i - 1
        while j >= 0 and key(a[j]) > key(cur):      # strictly greater -> stable
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a

for a in ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], [5, 5, 5, 5, 5], [2, 3, 1, 3, 2, 1, 1, 3]):
    print("Input :", a)
    print("Output:", insertion_sort(a))

pairs = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
print("\nStability check (sort by number only):", pairs)
print("Result:", insertion_sort(pairs, key=lambda p: p[0]))
print("Equal keys keep their original order -> insertion sort is stable")
