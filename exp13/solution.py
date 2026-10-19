def climb(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

for n in (4, 3, 10):
    print(f"n = {n} -> {climb(n)}")
