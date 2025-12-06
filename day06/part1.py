import unittest
import re
from functools import reduce


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

        out = 4277556

        self.assertEqual(process(test_in), out)


def transpose_lists_to_int(M):
    return [[int(M[j][i]) for j in range(len(M))] for i in range(len(M[0]))]


OPERATOR = {"*": int.__mul__, "+": int.__add__}


def process(input: str):
    total = 0

    orig_matrix = []
    for row in input.splitlines():
        orig_matrix.append([s.strip() for s in re.split(r"\s", row) if s])

    operators = orig_matrix[-1:][0]
    nums_only = orig_matrix[:-1]
    print(operators)
    print(nums_only)

    transp_nums = transpose_lists_to_int(nums_only)
    print(transp_nums)

    for i, prob in enumerate(transp_nums):
        total += reduce(OPERATOR[operators[i]], prob)

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
