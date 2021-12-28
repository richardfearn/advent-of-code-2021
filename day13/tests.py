import unittest

import day13
import utils

PART_1_EXAMPLE = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

PART_2_EXAMPLE_ANSWER = """
#####
#...#
#...#
#...#
#####
"""

PART_2_INPUT_ANSWER = """
.##....##.####..##..#....#..#.###....##
#..#....#....#.#..#.#....#..#.#..#....#
#.......#...#..#....#....#..#.#..#....#
#.##....#..#...#.##.#....#..#.###.....#
#..#.#..#.#....#..#.#....#..#.#....#..#
.###..##..####..###.####..##..#.....##.
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(17, day13.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(695, day13.part_1_answer(utils.read_input_lines(13)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            PART_2_EXAMPLE_ANSWER.strip(),
            day13.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(
            PART_2_INPUT_ANSWER.strip(),
            day13.part_2_answer(utils.read_input_lines(13)))
