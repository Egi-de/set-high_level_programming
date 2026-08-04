#!/usr/bin/python3
"""Module that solves the N Queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Return True if placing a queen at (row, col) is non-attacking."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively place queens row by row, collecting solutions."""
    if row == n:
        solution = [[r, board[r]] for r in range(n)]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Parse arguments and print every solution to N Queens."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
