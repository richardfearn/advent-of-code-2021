import unittest

import day25
import utils

PART_1_EXAMPLE_1 = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""

PART_1_EXAMPLE_2_INITIAL = "...>>>>>..."

PART_1_EXAMPLE_2_AFTER_1_STEP = "...>>>>.>.."

PART_1_EXAMPLE_2_AFTER_2_STEPS = "...>>>.>.>."

PART_1_EXAMPLE_3_BEFORE = """
..........
.>v....v..
.......>..
..........
"""

PART_1_EXAMPLE_3_AFTER = """
..........
.>........
..v....v>.
..........
"""

PART_1_EXAMPLE_4 = """
Initial state:
...>...
.......
......>
v.....>
......>
.......
..vvv..

After 1 step:
..vv>..
.......
>......
v.....>
>......
.......
....v..

After 2 steps:
....v>.
..vv...
.>.....
......>
v>.....
.......
.......

After 3 steps:
......>
..v.v..
..>v...
>......
..>....
v......
.......

After 4 steps:
>......
..v....
..>.v..
.>.v...
...>...
.......
v......
"""

PART_1_EXAMPLE_1_MULTI_STEP = """
Initial state:
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>

After 1 step:
....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v

After 2 steps:
>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv.

After 3 steps:
v>v.v>.>v.
v...>>.v.v
>vv>.>v>..
>>v>v.>.v>
..>....v..
.>.>v>v..v
..v..v>vv>
v.v..>>v..
.v>....v..

After 4 steps:
v>..v.>>..
v.v.>.>.v.
>vv.>>.v>v
>>.>..v>.>
..v>v...v.
..>>.>vv..
>.v.vv>v.v
.....>>vv.
vvv>...v..

After 5 steps:
vv>...>v>.
v.v.v>.>v.
>.v.>.>.>v
>v>.>..v>>
..v>v.v...
..>.>>vvv.
.>...v>v..
..v.v>>v.v
v.v.>...v.

...

After 10 steps:
..>..>>vv.
v.....>>.v
..v.v>>>v>
v>.>v.>>>.
..v>v.vv.v
.v.>>>.v..
v.v..>v>..
..v...>v.>
.vv..v>vv.

...

After 20 steps:
v>.....>>.
>vv>.....v
.>v>v.vv>>
v>>>v.>v.>
....vv>v..
.v.>>>vvv.
..v..>>vv.
v.v...>>.v
..v.....v>

...

After 30 steps:
.vv.v..>>>
v>...v...>
>.v>.>vv.>
>v>.>.>v.>
.>..v.vv..
..v>..>>v.
....v>..>v
v.v...>vv>
v.v...>vvv

...

After 40 steps:
>>v>v..v..
..>>v..vv.
..>>>v.>.v
..>>>>vvv>
v.....>...
v.v...>v>>
>vv.....v>
.>v...v.>v
vvv.v..v.>

...

After 50 steps:
..>>v>vv.v
..v.>>vv..
v.>>v>>v..
..>>>>>vv.
vvv....>vv
..v....>>>
v>.......>
.vv>....v>
.>v.vv.v..

...

After 55 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv...>..>
>vv.....>.
.>v.vv.v..

After 56 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv....>.>
>vv......>
.>v.vv.v..

After 57 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v..

After 58 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v..
"""


def parse_multi_step_example(example):
    states = utils.group_lines(example)
    states = [state for state in states if state != ['...']]
    initial_state = states[0][1:]
    states = states[1:]
    return initial_state, list(parse_state(state) for state in states)


def parse_state(state):
    num_steps = int(state[0].split(" ")[1])
    grid = state[1:]
    return num_steps, grid


class Part1Tests(unittest.TestCase):

    def test_step_example_2(self):
        initial_state = [PART_1_EXAMPLE_2_INITIAL]
        states = [
            (1, [PART_1_EXAMPLE_2_AFTER_1_STEP]),
            (2, [PART_1_EXAMPLE_2_AFTER_2_STEPS]),
        ]
        self._test_multi_step_example(initial_state, states)

    def test_step_example_3(self):
        initial_state = utils.to_lines(PART_1_EXAMPLE_3_BEFORE)
        states = [
            (1, utils.to_lines(PART_1_EXAMPLE_3_AFTER)),
        ]
        self._test_multi_step_example(initial_state, states)

    def test_step_example_4(self):
        initial_state, states = parse_multi_step_example(PART_1_EXAMPLE_4)
        self._test_multi_step_example(initial_state, states)

    def test_step_example_1_multi_step(self):
        initial_state, states = parse_multi_step_example(PART_1_EXAMPLE_1_MULTI_STEP)
        self._test_multi_step_example(initial_state, states)

    def _test_multi_step_example(self, initial_state, states):
        num_steps = 0
        state = initial_state
        for after_steps, expected_state in states:
            with self.subTest(after_steps=after_steps):
                while num_steps < after_steps:
                    state = day25.step(state)
                    num_steps += 1
                self.assertEqual(expected_state, state)

    def test_example_1(self):
        self.assertEqual(58, day25.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_with_input(self):
        self.assertEqual(432, day25.part_1_answer(utils.read_input_lines(25)))
