def solve_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[r // 3 * 3 + c // 3].add(v)

    def bt(k):
        if k == len(empties):
            return True
        r, c = empties[k]
        b = r // 3 * 3 + c // 3
        for v in "123456789":
            if v in rows[r] or v in cols[c] or v in boxes[b]:
                continue
            board[r][c] = v
            rows[r].add(v); cols[c].add(v); boxes[b].add(v)
            if bt(k + 1):
                return True
            board[r][c] = "."
            rows[r].discard(v); cols[c].discard(v); boxes[b].discard(v)
        return False

    return bt(0)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def show(b):
    for i, row in enumerate(b):
        if i % 3 == 0 and i:
            print("------+-------+------")
        print(" ".join(" ".join(row[j:j + 3]) + (" |" if j < 6 else "") for j in range(0, 9, 3)))

print("Input board:")
show(board)
print("\nSolved:", solve_sudoku(board))
show(board)
