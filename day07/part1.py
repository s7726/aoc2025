import unittest
import re
from copy import deepcopy


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

        out = 21

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


def process_board(board, starts: list | set):
    splits = 0

    if len(board) == 1:
        for start in starts:
            board[0][start] = "|"
        return board, splits

    new_starts = []
    for start in starts:
        if board[0][start] == "^":
            splits += 1
            board[0][start - 1] = "|"
            board[0][start + 1] = "|"
            new_starts.extend([start - 1, start + 1])
        else:
            board[0][start] = "|"
            new_starts.append(start)
    print("".join(board[0]))
    end_board, new_splits = process_board(board[1:], set(new_starts))
    splits += new_splits
    if not end_board:
        print("NO END BOARD")
    new_board = board[:1] + end_board

    return new_board, splits


def process(input: str):
    total = 0

    start = 0
    board = [list(l) for l in input.splitlines()]
    print_board(board)

    start = board[0].index("S")
    new_board, total = process_board(board[1:], [start])
    print_board(board[:1] + new_board)

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
