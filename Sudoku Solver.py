def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(grid):
    row, col = find_empty_location(grid)

    if row is None:
        return True

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def get_user_input():
    grid = []
    print("Enter the Sudoku puzzle row by row (use '0' for empty cells):")
    for _ in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

if __name__ == "__main__":
    # Get unsolved Sudoku puzzle from user
    puzzle = get_user_input()

    print("\nUnsolved Sudoku puzzle:")
    print_grid(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku puzzle:")
        print_grid(puzzle)
    else:
        print("\nNo solution exists for the Sudoku puzzle.")
