#!/usr/bin/python3
"""N queens in a N by N chessboard placed without attacking each other"""
import sys


if __name__ == "__main__":
    """main"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    else:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)


def issafe(board, row=0, col=0):
    """check if two queens not attacking or attacking each other"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        j -= 1
        i -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def place_queen(board, col=0):
    """Placing a queen where safe"""
    if col >= N:
        print_board(board)
        return True
    res = False
    for i in range(N):
        if issafe(board, i, col):
            board[i][col] = 1

            res = place_queen(board, col + 1) or res

            board[i][col] = 0
    return res


def print_board(board):
    """print the indices they are placed"""
    board_indices = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board_indices.append([i, j])
                break
    print(board_indices)


def n_queens():
    """Create board and solve the solution"""
    board = []
    for row in range(N):
        board.append([0] * N)
    place_queen(board, 0)


n_queens()
