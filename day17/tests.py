import unittest

import day17
import utils

PART_1_EXAMPLE = "target area: x=20..30, y=-10..-5"


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(45, day17.part_1_answer(PART_1_EXAMPLE))

    def test_with_input(self):
        self.assertEqual(8911, day17.part_1_answer(utils.read_input(17)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(112, day17.part_2_answer(PART_1_EXAMPLE))

    def test_with_input(self):
        self.assertEqual(4748, day17.part_2_answer(utils.read_input(17)))
