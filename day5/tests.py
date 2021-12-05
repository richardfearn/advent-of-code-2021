import unittest

import day5
import utils

PART_1_EXAMPLE = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(5, day5.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(5145, day5.part_1_answer(utils.read_input_lines(5)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(12, day5.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(16518, day5.part_2_answer(utils.read_input_lines(5)))
