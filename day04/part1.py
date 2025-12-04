import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        out = 13

        self.assertEqual(process(test_in), out)


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end="")
        print()


DIRS_ANY = [
    (-1, -1),
    (0, -1),
    (+1, -1),
    (+1, 0),
    (+1, +1),
    (0, +1),
    (-1, +1),
    (-1, 0),
]


def point_in_bounds(board, point):
    return (point[0] >= 0 and point[0] <= (len(board) - 1)) and (
        point[1] >= 0 and point[1] <= (len(board[0]) - 1)
    )


def is_accessible(roll_map, position) -> bool:
    locations = [(position[0] + y, position[1] + x) for y, x in DIRS_ANY]

    valid_locations = [loc for loc in locations if point_in_bounds(roll_map, loc)]
    print(f"{valid_locations}")
    accessible = 0
    for loc in valid_locations:
        if roll_map[loc[0]][loc[1]] == "@":
            accessible += 1
    print(f"{position}: {accessible}")
    return accessible < 4


def process(input: str):
    total = 0
    roll_map = []

    for line in input.splitlines():
        roll_map.append(list(line))

    print_board(roll_map)

    accessible_rolls = 0

    for row in range(len(roll_map)):
        for col in range(len(roll_map[row])):
            if roll_map[row][col] == "@":
                accessible_rolls += is_accessible(roll_map, (row, col))

    total = accessible_rolls

    return total


def input_runner(input: str):
    """This exists to provide a cleaner place to feed puzzle specific arguments
    to the process function
    """

    return process(input)


if __name__ == "__main__":
    if unittest.main(exit=False).result.wasSuccessful():
        file_content = None
        with open("input.txt") as infile:
            file_content = infile.read()

        file_content = file_content[:-1]  # Strip trailing newline
        import time

        start_time = time.time()
        output = input_runner(file_content)

        print(f"=======  {(time.time() - start_time):.3f}s  ======")
        print(f"Ans: {output}")
