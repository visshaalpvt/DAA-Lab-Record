def selection_sort(a, trace=False):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
        if trace:
            print(f"  pass {i + 1}: smallest = {a[i]} placed at index {i} -> {a}")
    return a

print("Step by step for [5, 2, 9, 1, 5, 6]:")
selection_sort([5, 2, 9, 1, 5, 6], trace=True)
print()
for a in ([], [1], [7, 7, 7, 7], [-5, -1, -3, -2, -4], [5, 2, 9, 1, 5, 6], [10, 8, 6, 4, 2], [1, 2, 3, 4, 5]):
    print("Input :", a, "-> Output:", selection_sort(a))
