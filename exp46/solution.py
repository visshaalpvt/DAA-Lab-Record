def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m
    a, b = divmod(x, p)
    c, d = divmod(y, p)
    ac, bd = karatsuba(a, c), karatsuba(b, d)
    mid = karatsuba(a + b, c + d) - ac - bd
    return ac * p * p + mid * p + bd

x, y = 1234, 5678
print(f"Karatsuba: {x} x {y} = {karatsuba(x, y)}")
print(f"Check    : {x} x {y} = {x * y}")
