import unittest
import re
from operator import attrgetter
from itertools import pairwise
from copy import copy


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

        out = 14

        self.assertEqual(process(test_in), out)


def combine_maybe(r1: range, r2: range):
    if r2.start < r1.stop:
        return [range(r1.start, r2.stop)]
    return [r1, r2]


def process(input: str):
    total = 0
    fresh_ranges_raw = []

    fresh_ranges_raw, _ = input.split("\n\n")

    fresh_ranges = [
        range(int(r[0]), int(r[1]) + 1)
        for r in (fr.split("-") for fr in fresh_ranges_raw.splitlines())
    ]

    fresh_ranges.sort(key=attrgetter("stop"))

    new_ranges = copy(fresh_ranges)
    found_overlap = True
    while found_overlap:
        cycle_ranges = set()
        found_overlap = False
        for pair in pairwise(new_ranges):
            c = combine_maybe(*pair)
            cycle_ranges.add(c[0])
            if len(c) == 1:
                found_overlap = True
        if found_overlap:
            new_ranges = sorted(list(cycle_ranges), key=attrgetter("stop"))
        print(new_ranges, flush=True)

    for r in new_ranges:
        total += r.stop - r.start

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
