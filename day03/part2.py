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


"""
I was stuck on this for way too long, not sure why it seems a little obvious
now I broke down and watched https://www.youtube.com/watch?v=XlDIGtl8iSE to
finally work out how to move forward. This was implemented after watching
that, but not as a direct copy. Thanks @HyperNeutrino I was close, but
apparently needed a push (hint in the form of the answer 🤣)

Maybe not... So apparently I had a hunk of test code that was failing, because
it was broken! Which meant that it was never going to work... So I very well
may have had this working for some time and just not known it! Extremely
frustrating! Oh well, who knows when I actually fixed it and in how many ways
it may have been correct prior to this. Lesson learned I guess 🤷‍♂️
"""


def reduce_to_digits(bank: list, length) -> int:
    val = 0
    jolts = ""
    bank_int = list(map(int, bank))
    for start in range(length - 1):
        digit = max(bank_int[: start - (length - 1)])
        bank_int = bank_int[bank_int.index(digit) + 1 :]
        jolts += str(digit)
    jolts += str(max(bank_int))

    val = int(jolts)

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
