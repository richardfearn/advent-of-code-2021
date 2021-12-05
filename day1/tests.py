import unittest

import day1
import utils

PART_1_EXAMPLE = """
199
200
208
210
200
207
240
269
260
263
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(7, day1.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1548, day1.part_1_answer(utils.read_input_lines(1)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(5, day1.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1589, day1.part_2_answer(utils.read_input_lines(1)))
