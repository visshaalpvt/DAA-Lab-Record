def game_of_life(b):
    m, n = len(b), len(b[0])
    for i in range(m):
        for j in range(n):
            live = sum(b[x][y] & 1
                       for x in range(max(0, i - 1), min(m, i + 2))
                       for y in range(max(0, j - 1), min(n, j + 2)) if (x, y) != (i, j))
            if b[i][j] == 1 and live in (2, 3):
                b[i][j] = 3
            elif b[i][j] == 0 and live == 3:
                b[i][j] = 2
    for i in range(m):
        for j in range(n):
            b[i][j] >>= 1
    return b

for board in ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[1, 1], [1, 0]]):
    print("Input :", board)
    print("Output:", game_of_life([row[:] for row in board]))
