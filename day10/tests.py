import unittest

import day10
import utils

PART_1_EXAMPLE = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(26397, day10.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(290691, day10.part_1_answer(utils.read_input_lines(10)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(288957, day10.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2768166558, day10.part_2_answer(utils.read_input_lines(10)))
