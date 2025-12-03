import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

        out = 1227775554

        self.assertEqual(process(test_in), out)


def check_repeat(val):
    if val[: len(val) // 2] == val[len(val) // 2 :]:
        return 1
    return 0


def process(input: str):
    total = 0

    ranges = [(y[0], y[1]) for y in (x.split("-") for x in input.split(","))]
    print(ranges)

    for r in ranges:
        start = int(r[0])
        end = int(r[1])
        for val in range(start, end + 1):
            repeat = check_repeat(str(val))
            if repeat:
                total += val
            print(f"({start}, {end}) -> {val}:{repeat} == {total}")

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
