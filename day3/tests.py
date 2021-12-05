import unittest

import day3
import utils

PART_1_EXAMPLE = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(198, day3.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2648450, day3.part_1_answer(utils.read_input_lines(3)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(230, day3.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2845944, day3.part_2_answer(utils.read_input_lines(3)))
