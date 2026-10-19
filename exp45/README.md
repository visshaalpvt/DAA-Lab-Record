# Exp 45: Strassen's Matrix Multiplication (2x2)

## Aim
To multiply two 2x2 matrices with Strassen's algorithm using 7 multiplications instead of 8.

## Algorithm
1. Compute M1 = (A11 + A22)(B11 + B22), M2 = (A21 + A22)B11, M3 = A11(B12 - B22), M4 = A22(B21 - B11)
2. M5 = (A11 + A12)B22, M6 = (A21 - A11)(B11 + B12), M7 = (A12 - A22)(B21 + B22)
3. C11 = M1 + M4 - M5 + M7, C12 = M3 + M5, C21 = M2 + M4, C22 = M1 - M2 + M3 + M6
4. Verify against ordinary multiplication

## Input
```
A = [[1,7],[3,5]], B = [[1,3],[7,5]]
A = [[1,7],[3,5]], B = [[6,8],[4,2]]
```

## Program
[`solution.py`](solution.py)

```python
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
```

## Output
```
A=[[1, 7], [3, 5]], B=[[1, 3], [7, 5]]
Strassen C = [[50, 38], [38, 34]] | Normal C = [[50, 38], [38, 34]] | Match: True
A=[[1, 7], [3, 5]], B=[[6, 8], [4, 2]]
Strassen C = [[34, 22], [38, 34]] | Normal C = [[34, 22], [38, 34]] | Match: True
```

## Screenshot
![Output screenshot](output.png)

## Result
The program for **Strassen's Matrix Multiplication (2x2)** was implemented and executed successfully, and the output shown above was obtained for all the given test cases.

> **Note:** The sheet's expected result [[18,14],[62,66]] is not the product of the given matrices. A x B for test case 1 is [[34,22],[38,34]]; the program's Strassen result is verified against ordinary multiplication.

## Time and Space Complexity
| | Complexity |
|---|---|
| **Time** | O(n^2.81) in general (7 multiplications for 2x2) |
| **Space** | O(n^2) |
