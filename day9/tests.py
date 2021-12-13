import unittest

import day9
import utils

PART_1_EXAMPLE = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(15, day9.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(603, day9.part_1_answer(utils.read_input_lines(9)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1134, day9.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(786780, day9.part_2_answer(utils.read_input_lines(9)))
