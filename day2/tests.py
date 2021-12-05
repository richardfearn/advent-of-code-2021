import unittest

import day2
import utils

PART_1_EXAMPLE = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(150, day2.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2215080, day2.part_1_answer(utils.read_input_lines(2)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(900, day2.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1864715580, day2.part_2_answer(utils.read_input_lines(2)))
