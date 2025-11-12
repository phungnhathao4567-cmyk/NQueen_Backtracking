# ------------------------------------------------------------
# BÀI TOÁN N-QUEEN – THUẬT TOÁN BACKTRACKING
# Phùng Nhật Hào – Nhóm PTTKGT
# ------------------------------------------------------------

# Ý tưởng:
# Đặt N quân hậu (Queen) trên bàn cờ NxN sao cho
# không có 2 quân nào tấn công nhau theo hàng, cột, hay đường chéo.

def print_board(board):
    n = len(board)
    for r in range(n):
        line = ""
        for c in range(n):
            if board[r] == c:
                line += "♛ "
            else:
                line += "· "
        print(line)
    print("\n")

def solve_n_queens(n):
    solutions = []
    cols = set()      # cột đã có hậu
    diag1 = set()     # đường chéo chính (r + c)
    diag2 = set()     # đường chéo phụ (r - c)
    board = [-1] * n  # board[r] = vị trí cột của hậu ở hàng r

    def backtrack(r):
        if r == n:
            solutions.append(board.copy())
            return
        for c in range(n):
            if c in cols or (r + c) in diag1 or (r - c) in diag2:
                continue
            # đặt hậu
            board[r] = c
            cols.add(c)
            diag1.add(r + c)
            diag2.add(r - c)
            backtrack(r + 1)
            # bỏ hậu
            cols.remove(c)
            diag1.remove(r + c)
            diag2.remove(r - c)

    backtrack(0)
    return solutions


# ----------- CHƯƠNG TRÌNH CHÍNH -------------
if __name__ == "__main__":
    n = int(input("Nhập N (số quân hậu): "))
    results = solve_n_queens(n)

    print(f"\nTổng số lời giải: {len(results)}\n")

    # In ra 1 số lời giải (giới hạn để dễ xem)
    for idx, sol in enumerate(results, start=1):
        print(f"Lời giải {idx}:")
        print_board(sol)
        if idx >= 3:  # chỉ in 3 lời giải đầu tiên để dễ đọc
            break
