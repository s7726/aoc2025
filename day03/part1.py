import unittest
import re
from itertools import combinations


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """987654321111111
811111111111119
234234234234278
818181911112111"""

        out = 357

        self.assertEqual(process(test_in), out)


def process(input: str):
    total = 0

    for bank in input.splitlines():
        possible = combinations([x for x in list(bank)], 2)
        vals = [int("".join(x)) for x in list(possible)]
        print(f"{vals=}")
        max_val = max(vals)
        print(f"{max_val=}")
        total += max_val

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
