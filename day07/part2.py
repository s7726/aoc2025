import unittest
import re
from functools import cache


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

        out = 40

        self.assertEqual(process(test_in), out)


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end="")
        print()


@cache
def process_board(board, start: int):
    timelines = 0

    if len(board) == 1:
        return 1

    if board[0][start] == "^":
        timelines += process_board(board[1:], start - 1)
        timelines += process_board(board[1:], start + 1)
    else:
        timelines += process_board(board[1:], start)

    return timelines


def process(input: str):
    total = 0

    start = 0
    board = tuple([tuple(l) for l in input.splitlines()])
    print_board(board)

    start = board[0].index("S")
    total = process_board(board[1:], start)

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
