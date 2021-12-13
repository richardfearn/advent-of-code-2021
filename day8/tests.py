import unittest

import day8
import utils

PART_1_EXAMPLE_1 = """
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
"""

PART_1_EXAMPLE_2 = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


class Part1Tests(unittest.TestCase):

    def test_example_2(self):
        self.assertEqual(26, day8.part_1_answer(PART_1_EXAMPLE_2))

    def test_with_input(self):
        self.assertEqual(495, day8.part_1_answer(utils.read_input(8)))


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(5353, day8.part_2_answer(PART_1_EXAMPLE_1))

    def test_example_2(self):
        self.assertEqual(61229, day8.part_2_answer(PART_1_EXAMPLE_2))

    def test_with_input(self):
        self.assertEqual(1055164, day8.part_2_answer(utils.read_input(8)))
