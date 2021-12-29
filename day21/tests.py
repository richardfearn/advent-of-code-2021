import unittest

import day21
import utils

PART_1_EXAMPLE = """
Player 1 starting position: 4
Player 2 starting position: 8
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(739785, day21.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(576600, day21.part_1_answer(utils.read_input_lines(21)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(444356092776315, day21.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(131888061854776, day21.part_2_answer(utils.read_input_lines(21)))
