import unittest

import day15
import utils

PART_1_EXAMPLE = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(40, day15.total_risk(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(673, day15.total_risk(utils.read_input_lines(15)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(315, day15.total_risk(utils.to_lines(PART_1_EXAMPLE), True))

    def test_with_input(self):
        # 2908 is too high
        self.assertEqual(2893, day15.total_risk(utils.read_input_lines(15), True))
