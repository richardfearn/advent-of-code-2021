import unittest

import day14
import utils

PART_1_EXAMPLE = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1588, day14.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(4517, day14.part_1_answer(utils.read_input_lines(14)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2188189693529, day14.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(4704817645083, day14.part_2_answer(utils.read_input_lines(14)))
