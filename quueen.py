def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "-" for cell in row))
    print()

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    if row == len(board):
        # All queens are placed, solution found
        print_board(board)
        return 1

    count = 0
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen

            # Recur for the next row
            count += solve_n_queens(board, row + 1)

            board[row][col] = 0  # Backtrack and remove the queen

    return count

def main():
    N = 8
    board = [[0] * N for _ in range(N)]

    solutions = solve_n_queens(board, 0)

    print("Total solutions:", solutions)

if __name__ == "__main__":
    main()
