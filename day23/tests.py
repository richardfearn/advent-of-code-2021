import unittest

import day23
import utils

PART_1_EXAMPLE = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

PART_2_EXAMPLE = """
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
"""

PART_2_EXTRA_LINES = [
    "  #D#C#B#A#",
    "  #D#B#A#C#",
]


class GeneralTests(unittest.TestCase):

    def test_find_amphipod_that_can_leave_room(self):
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("..", "A"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room(".A", "A"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("AA", "A"))

        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("..", "B"))
        self.assertEqual(1, day23.find_amphipod_that_can_leave_room(".A", "B"))
        self.assertEqual(0, day23.find_amphipod_that_can_leave_room("AA", "B"))

        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("....", "A"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("...A", "A"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("..AA", "A"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room(".AAA", "A"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("AAAA", "A"))

        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("....", "B"))
        self.assertEqual(3, day23.find_amphipod_that_can_leave_room("...A", "B"))
        self.assertEqual(2, day23.find_amphipod_that_can_leave_room("..AA", "B"))
        self.assertEqual(1, day23.find_amphipod_that_can_leave_room(".AAA", "B"))
        self.assertEqual(0, day23.find_amphipod_that_can_leave_room("AAAA", "B"))

        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("....", "B"))
        self.assertEqual(3, day23.find_amphipod_that_can_leave_room("...A", "B"))
        self.assertEqual(2, day23.find_amphipod_that_can_leave_room("..AB", "B"))
        self.assertEqual(1, day23.find_amphipod_that_can_leave_room(".AAB", "B"))
        self.assertEqual(0, day23.find_amphipod_that_can_leave_room("AAAB", "B"))

        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("....", "B"))
        self.assertEqual(None, day23.find_amphipod_that_can_leave_room("...B", "B"))
        self.assertEqual(2, day23.find_amphipod_that_can_leave_room("..BA", "B"))
        self.assertEqual(1, day23.find_amphipod_that_can_leave_room(".BBA", "B"))
        self.assertEqual(0, day23.find_amphipod_that_can_leave_room("BBBA", "B"))

    def test_find_room_position_for_amphipod(self):
        self.assertEqual(1, day23.find_room_position_for_amphipod("A", ".."))
        self.assertEqual(0, day23.find_room_position_for_amphipod("A", ".A"))
        self.assertEqual(None, day23.find_room_position_for_amphipod("A", "AA"))
        self.assertEqual(None, day23.find_room_position_for_amphipod("A", ".B"))
        self.assertEqual(None, day23.find_room_position_for_amphipod("A", "BB"))


class Part1Tests(unittest.TestCase):

    def test_manual(self):
        self.assertEqual(12521, day23.manual_part_1_example(utils.to_lines(PART_1_EXAMPLE)))

    def test_example(self):
        self.assertEqual(12521, day23.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(16489, day23.part_1_answer(utils.read_input_lines(23)))


class Part2Tests(unittest.TestCase):

    def test_manual(self):
        self.assertEqual(44169, day23.manual_part_2_example(utils.to_lines(PART_2_EXAMPLE)))

    def test_example(self):
        self.assertEqual(44169, day23.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        input_lines = utils.read_input_lines(23)
        input_lines = input_lines[:3] + PART_2_EXTRA_LINES + input_lines[3:]
        self.assertEqual(43413, day23.part_2_answer(input_lines))
