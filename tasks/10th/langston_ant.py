import unittest


class LangtonsAntTest(unittest.TestCase):
    def test_ant(self):
        # At a white square, turn 90° right, flip the color of the square, move forward one unit
        # At a black square, turn 90° left, flip the color of the square, move forward one unit
        # Dir : 0 - north, 1 - east, 2 - south, 3 - west
        # 1 white 0 black
        self.assertEqual(ant([[1]], 0, 0, 1, 0), [[0, 0]])
        self.assertEqual(ant([[0]], 0, 0, 1, 0), [[0, 1]])
        self.assertEqual(ant([[1]], 0, 0, 3, 0), [[0, 1], [0, 1]])


direction_map = {0: 'north', 1: 'east', 2: 'south', 3: 'west'}


def ant(grid, column, row, n, direction=0):
    if n == 0:
        return grid

    state = grid[row][column]

    # direction
    if state == 1:
        direction = direction + 1 if direction + 1 <= 3 else 0
        grid[row][column] = 0
    else:
        direction = direction - 1 if direction - 1 >= 0 else 3
        grid[row][column] = 1

    # row, column
    if direction == 1:
        column = column + 1
        grid[row].append(0)
    elif direction == 3:
        grid[row].insert(0, 0)

    elif direction == 0:
        column = 0
        grid.insert(0, [0])

    elif direction == 2:
        column = 0
        row = row + 1
        grid.append([0])

    return ant(grid, column, row, n - 1, direction)


if __name__ == '__main__':
    unittest.main()
