from os import curdir
import unittest
import re
from itertools import combinations


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """987654321111111
811111111111119
234234234234278
818181911112111"""

        out = 3121910778619

        self.assertEqual(process(test_in), out)

        for line in test_in.splitlines():
            with self.subTest():
                self.assertEqual(process(line), out)

    def test_pieces(self):
        test_in = [
            ("987654321111111", 987654321111),
            ("811111111111119", 811111111119),
            ("234234234234278", 434234234278),
            ("818181911112111", 888911112111),
        ]

        for line in test_in:
            with self.subTest(line[0]):
                self.assertEqual(process(line[0]), line[1])


def reduce_to_digits(bank: list, length) -> int:
    val = 0

    cur_index = 0
    big_stack = bank[:length]
    slide_len = len(bank) - length + 1
    start = 0
    for i in range(0, len(big_stack)):
        start = max(i, start)

        end = min(start + slide_len, len(bank))

        for j in range(start, end):
            if int(big_stack[i]) < int(bank[j]):
                big_stack[i] = bank[j]
                start = j + 1

    val = int("".join(big_stack))

    return val


def process(input: str):
    total = 0

    for bank in input.splitlines():
        total += reduce_to_digits(list(bank), 12)

    return total


def input_runner(input):
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
