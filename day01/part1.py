from os import DirEntry, curdir
import unittest
import re


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

        out = 3

        start = 0
        end = 99

        start_num = 50

        self.assertEqual(process(test_in, start, end, start_num), out)


def process(input, start, end, start_num):
    total = 0
    cur_index = start_num
    for line in input.splitlines():
        direction = line[:1]
        increment = int(line[1:])
        new_index = cur_index
        if direction == "R":
            new_index = cur_index + increment

        if direction == "L":
            new_index = cur_index - increment
        adjusted_index = new_index
        while adjusted_index > end:
            adjusted_index = start + (adjusted_index - end - 1)
        while adjusted_index < start:
            adjusted_index = end + 1 - (start - adjusted_index)

        print(
            f"{cur_index} {direction} {increment} = {new_index} => {adjusted_index}\n"
        )

        if adjusted_index == 0:
            total += 1
        cur_index = adjusted_index
    return total


def input_runner(input):
    """This exists to provide a cleaner place to feed puzzle specific arguments
    to the process function
    """

    start = 0
    end = 99

    start_num = 50

    return process(input, start, end, start_num)


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
