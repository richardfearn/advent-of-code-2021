import unittest

import day11
import utils

PART_1_EXAMPLE = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        input_lines = utils.to_lines(PART_1_EXAMPLE)
        for steps, flashes in ((10, 204), (100, 1656)):
            with self.subTest(steps=steps, flashes=flashes):
                self.assertEqual(flashes, day11.part_1_answer(input_lines, steps))

    def test_with_input(self):
        self.assertEqual(1625, day11.part_1_answer(utils.read_input_lines(11), 100))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(195, day11.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(244, day11.part_2_answer(utils.read_input_lines(11)))
