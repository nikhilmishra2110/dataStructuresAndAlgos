grid = [[4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2]]


def countNegatives(grid):
    number_of_rows = len(grid)  # rows
    number_of_cols = len(grid[0])  # columns
    r = 0
    c = number_of_cols -1
    count = 0
    print(grid)
    print("number_of_rows is >> ", number_of_rows)
    print("number_of_cols is >> ", number_of_cols)

    print("r is >> ", r)
    print("c is >> ", c)
    print()

    while r < number_of_rows and c >= 0:
        print("I am at ", grid[r][c])
        if grid[r][c] < 0:
            count += number_of_rows - r
            c -= 1
        else:
            r += 1
        print("r is >> ", r)
        print("c is >> ", c)
        print("count is >> ", count)
        print()
    return count


print(countNegatives(grid))
