import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

        out = 3

        self.assertEqual(process(test_in), out)


def process(input: str):
    total = 0
    fresh_ranges_raw = []
    ingredients_available = []

    fresh_ranges_raw, ingredients_available = input.split("\n\n")

    fresh_ranges = [
        range(int(r[0]), int(r[1]) + 1)
        for r in (fr.split("-") for fr in fresh_ranges_raw.splitlines())
    ]

    for ingredient in ingredients_available.splitlines():
        total += any(int(ingredient) in fresh_range for fresh_range in fresh_ranges)

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
