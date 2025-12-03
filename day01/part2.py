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

        out = 6

        start = 0
        end = 99

        start_num = 50

        self.assertEqual(process(test_in, start, end, start_num), out)

    def test_example2(self):
        test_in = """R1000"""

        out = 10

        start = 0
        end = 99

        start_num = 50

        self.assertEqual(process(test_in, start, end, start_num), out)

    def test_example3(self):
        test_in = """R393"""

        out = 4

        start = 0
        end = 99

        start_num = 43

        self.assertEqual(process(test_in, start, end, start_num), out)

    def test_example4(self):
        test_in = """L50
R1"""

        out = 1

        start = 0
        end = 99

        start_num = 50

        self.assertEqual(process(test_in, start, end, start_num), out)

    def test_example5(self):
        test_in = """R50
L1"""

        out = 1

        start = 0
        end = 99

        start_num = 50

        self.assertEqual(process(test_in, start, end, start_num), out)

    def test_example6(self):
        tests_in = [("L250", 3), ("L251", 3), ("R250", 3), ("R251", 3)]

        start = 0
        end = 99

        start_num = 50

        for test in tests_in:
            with self.subTest(test[0]):
                self.assertEqual(process(test[0], start, end, start_num), test[1])


def process(input, start, end, start_num):
    total = 0
    cur_index = start_num
    for line in input.splitlines():
        direction = line[:1]
        increment = int(line[1:])
        new_index = cur_index
        # if direction == "R":
        inc = +1

        if direction == "L":
            inc = -1

        for _ in range(increment):
            cur_index += inc
            if cur_index == start - 1:
                cur_index = end
            if cur_index == end + 1:
                cur_index = start
            if cur_index == 0:
                total += 1

        print(f"{new_index} {direction} {increment} = {cur_index}  {total=}")

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
