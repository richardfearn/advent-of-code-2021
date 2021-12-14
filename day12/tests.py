import unittest

import day12
import utils

PART_1_EXAMPLE_1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

PART_1_EXAMPLE_2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

PART_1_EXAMPLE_3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(10, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(19, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_example_3(self):
        self.assertEqual(226, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE_3)))

    def test_with_input(self):
        self.assertEqual(4749, day12.part_1_answer(utils.read_input_lines(12)))


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(36, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(103, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_example_3(self):
        self.assertEqual(3509, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE_3)))

    def test_with_input(self):
        self.assertEqual(123054, day12.part_2_answer(utils.read_input_lines(12)))
