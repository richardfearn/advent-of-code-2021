import unittest

import day7
import utils

PART_1_EXAMPLE = "16,1,2,0,4,2,7,1,2,14"


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(37, day7.part_1_answer(PART_1_EXAMPLE))

    def test_with_input(self):
        self.assertEqual(364898, day7.part_1_answer(utils.read_input(7)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(168, day7.part_2_answer(PART_1_EXAMPLE))

    def test_with_input(self):
        self.assertEqual(104149091, day7.part_2_answer(utils.read_input(7)))
