import unittest

import day6
import utils

PART_1_EXAMPLE = "3,4,3,1,2"


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(26, day6.simulation(PART_1_EXAMPLE, 18))
        self.assertEqual(5934, day6.simulation(PART_1_EXAMPLE, 80))

    def test_with_input(self):
        self.assertEqual(362639, day6.simulation(utils.read_input(6), 80))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(26984457539, day6.simulation(PART_1_EXAMPLE, 256))

    def test_with_input(self):
        self.assertEqual(1639854996917, day6.simulation(utils.read_input(6), 256))
