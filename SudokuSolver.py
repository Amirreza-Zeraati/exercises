from pprint import pprint


def print_board(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple; (None, None) if there is none
    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # that number must not be repeated in the row, column, or 3x3 square that it appears in
    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of arrays, where each inner list is a row in puzzle
    row, col = print_board(puzzle)
    # if there's nowhere left, then we're done
    if row is None:
        return True
    # if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        # is not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1
    # if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False


board = [
    [3, 9, -1,      -1, 5, -1,      -1, -1, -1],
    [-1, -1, -1,     2, -1, -1,     -1, -1, 5],
    [-1, -1, -1,     7, 1, 9,       -1, 8, -1],

    [-1, 5, -1,      -1, 6, 8,      -1, -1, -1],
    [2, -1, 6,       -1, -1, 3,     -1, -1, -1],
    [-1, -1, -1,     -1, -1, -1,    -1, -1, 4],

    [5, -1, -1,     -1, -1, -1,      -1, -1, -1],
    [6, 7, -1,       1, -1, 5,       -1, 4, -1],
    [1, -1, 9,      -1, -1, -1,      2, -1, -1]]

print(solve_sudoku(board))
pprint(board)
