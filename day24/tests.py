import random
import unittest

import day24
import utils

ALL_VARIABLES = W, X, Y, Z = "w", "x", "y", "z"

PART_1_EXAMPLE_PROGRAM_1 = """
inp x
mul x -1
"""

PART_1_EXAMPLE_PROGRAM_2 = """
inp z
inp x
mul z 3
eql z x
"""

PART_1_EXAMPLE_PROGRAM_3 = """
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""

PART_1_EXAMPLE_MODEL_NUMBER = 13579246899999

PART_1_EXAMPLE_MODEL_NUMBER_Z_RESULT = 112265567

PART_1_ANSWER = 99598963999971

PART_2_ANSWER = 93151411711211


class GeneralTests(unittest.TestCase):

    def test_monad_interpreted_and_monad_hand_coded_are_equivalent(self):
        input_lines = utils.read_input_lines(24)
        i = 0
        while i < 50000:
            model_number = random.randint(11111111111111, 99999999999999 + 1)
            if "0" not in str(model_number):
                i += 1
                interpreted_result = day24.monad_interpreted(input_lines, model_number)
                hand_coded_result = day24.monad_hand_coded(model_number)
                self.assertEqual(interpreted_result, hand_coded_result)


class Part1Tests(unittest.TestCase):

    def test_run_program_example_1(self):
        expected = {W: 0, X: -9, Y: 0, Z: 0}
        self.assertEqual(expected, day24.run_program(utils.to_lines(PART_1_EXAMPLE_PROGRAM_1), [9]))

    def test_run_program_example_2(self):
        tests = [
            (10, 30, 1),
            (10, 40, 0),
        ]

        for a, b, z in tests:
            variables = day24.run_program(utils.to_lines(PART_1_EXAMPLE_PROGRAM_2), [a, b])
            with self.subTest(a=a, b=b, z=z, variables=variables):
                self.assertEqual(z, variables[Z])

    def test_run_program_example_3(self):
        for i in range(16):
            expected = dict(zip(ALL_VARIABLES, [int(d) for d in format(i, '04b')]))
            variables = day24.run_program(utils.to_lines(PART_1_EXAMPLE_PROGRAM_3), [i])
            with self.subTest(i=i, expected=expected, variables=variables):
                self.assertEqual(expected, variables)

    def test_monad_interpreted_with_example_model_number(self):
        self.assertEqual(
            PART_1_EXAMPLE_MODEL_NUMBER_Z_RESULT,
            day24.monad_interpreted(utils.read_input_lines(24), PART_1_EXAMPLE_MODEL_NUMBER))

    def test_monad_hand_coded_with_example_model_number(self):
        self.assertEqual(
            PART_1_EXAMPLE_MODEL_NUMBER_Z_RESULT,
            day24.monad_hand_coded(PART_1_EXAMPLE_MODEL_NUMBER))

    def test_search(self):
        self.assertEqual(PART_1_ANSWER, day24.part_1_answer())

    def test_monad_interpreted_with_answer(self):
        self.assertEqual(0, day24.monad_interpreted(utils.read_input_lines(24), PART_1_ANSWER))

    def test_monad_hand_coded_with_answer(self):
        self.assertEqual(0, day24.monad_hand_coded(PART_1_ANSWER))


class Part2Tests(unittest.TestCase):

    def test_search(self):
        self.assertEqual(PART_2_ANSWER, day24.part_2_answer())

    def test_monad_interpreted_with_answer(self):
        self.assertEqual(0, day24.monad_interpreted(utils.read_input_lines(24), PART_2_ANSWER))

    def test_monad_hand_coded_with_answer(self):
        self.assertEqual(0, day24.monad_hand_coded(PART_2_ANSWER))
