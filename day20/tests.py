import unittest

import day20
import utils

PART_1_EXAMPLE = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(35, day20.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 2))

    def test_with_input(self):
        self.assertEqual(5583, day20.part_1_answer(utils.read_input_lines(20), 2))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3351, day20.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 50))

    def test_with_input(self):
        self.assertEqual(19592, day20.part_1_answer(utils.read_input_lines(20), 50))
