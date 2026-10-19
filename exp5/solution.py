def find_max(a):
    m = a[0]
    for x in a[1:]:
        if x > m:
            m = x
    return m

for a in ([1, 2, 3, 4, 5], [7, 7, 7, 7, 7], [-10, 2, 3, -4, 5]):
    print("Input :", a)
    print("Output:", find_max(a))
