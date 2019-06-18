def ant(grid, column, row, n, direction=0):
    # grid[column][row]값 체크
    DIR = [0, 1, 2, 3]  # 북동남서

    WHITE = 1
    WHITE_DIR = 1
    BLACK = 0
    BLACK_DIR = -1

    if grid[row][column] == WHITE:
        # 방향전환
        dir_index = DIR.index(direction) + WHITE_DIR
        if dir_index == len(DIR):
            dir_index = 0
        next_direction = DIR[dir_index]

        # color변경
        grid[row][column] = BLACK

        # 이동
        if next_direction == 0:
            row = row - 1
        if next_direction == 1:
            column = column + 1
        if next_direction == 2:
            row = row + 1
        if next_direction == 3:
            column = column - 1
    else:
        # 방향전환
        dir_index = DIR.index(direction) + BLACK_DIR
        if dir_index == -1:
            dir_index = len(DIR) - 1
        next_direction = DIR[dir_index]

        # color변경
        grid[row][column] = WHITE

        # 이동
        if next_direction == 0:
            row = row - 1
        if next_direction == 1:
            column = column + 1
        if next_direction == 2:
            row = row + 1
        if next_direction == 3:
            column = column - 1

    # 갔던 영역인지 확인
    try:
        # 갔던 곳
        if row == -1:
            row = len(grid)
        if column == -1:
            column = len(grid[row])
        if grid[row][column] is not None:
            if grid[row][column] == 1:
                grid[row][column] = 0
            else:
                grid[row][column] = 1
    except:
        # 안갔던 곳이면 북쪽이면 prepend([0]) 남쪽이면 append([0]) column증가면 서쪽이면 prepend 왼쪽이면 append
        if next_direction == 0:
            grid.insert(len(grid), [0] * (len(grid) + 1))
        if next_direction == 1:
            grid[row].insert(len(grid[row]), 0)
        if next_direction == 2:
            grid.insert(len(grid), [0] * (len(grid) + 1))
        if next_direction == 3:
            grid[row].insert(0, 0)

    n = n - 1
    if n == 0:
        return grid
    else:
        return ant(grid, column, row, n, next_direction)


