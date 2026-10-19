def strassen_2x2(A, B):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
    m1 = (a + d) * (e + h)
    m2 = (c + d) * e
    m3 = a * (f - h)
    m4 = d * (g - e)
    m5 = (a + b) * h
    m6 = (c - a) * (e + f)
    m7 = (b - d) * (g + h)
    return [[m1 + m4 - m5 + m7, m3 + m5], [m2 + m4, m1 - m2 + m3 + m6]]

def normal(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

for A, B in (([[1, 7], [3, 5]], [[1, 3], [7, 5]]), ([[1, 7], [3, 5]], [[6, 8], [4, 2]])):
    C = strassen_2x2(A, B)
    print(f"A={A}, B={B}")
    print("Strassen C =", C, "| Normal C =", normal(A, B), "| Match:", C == normal(A, B))
