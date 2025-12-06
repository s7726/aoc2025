import enum
import unittest
import re
from functools import reduce


class TestPart(unittest.TestCase):
    def test_example(self):
        test_in = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

        out = 3263827

        self.assertEqual(process(test_in), out)


def transpose_lists(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def split_and_arrange(l, spacing):
    new_list = []
    for i, row in enumerate(l):
        cur = 0
        new_row = []
        for s, space in enumerate(spacing):
            new_row.append(list(l[i][cur : cur + space]))
            cur += space
        new_list.append(new_row)
    return new_list


def fill_ops(ops, lens):
    cur = ""
    filled = []
    for op in ops:
        if op != " ":
            cur = op
        filled.append(cur)
    return filled


def combine_trans(t):
    ct = []

    for s in t:
        num_list = []
        for col in range(len(s[0])):
            num = ""
            for j, row in enumerate(s):
                num += row[col]
            if num.strip():
                num_list.append(int(num))
        ct.append(num_list)

    return ct


OPERATOR = {"*": int.__mul__, "+": int.__add__}


def process(input: str):
    total = 0

    orig_rows = []
    for row in input.splitlines():
        orig_rows.append(row)

    operators = orig_rows[-1:][0]
    nums_only = orig_rows[:-1]
    print(operators)
    print(nums_only)

    #  Get the spacing of each column
    column_lens = [len(match) for match in re.findall(r"[\*\+]\s*", operators)]
    print(column_lens)

    arranged_nums = split_and_arrange(nums_only, column_lens)
    print(arranged_nums)

    trans = transpose_lists(arranged_nums)
    print(trans)

    combined_trans = combine_trans(trans)
    print(combined_trans)

    clean_ops = [op.strip() for op in re.findall(r".\s*", operators)]
    print(clean_ops)

    # Do the math on the properly arranged list/matrix
    for i, prob in enumerate(combined_trans):
        total += reduce(OPERATOR[clean_ops[i]], prob)

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
