import unittest

import day18
import utils

PART_1_SINGLE_EXPLODE_ACTION_EXAMPLES = [
    ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
    ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
    ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
    ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
]

PART_1_REDUCE_STEPS_EXAMPLE = """
after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
"""

PART_1_LIST_EXAMPLES = [
    ("[[[[1,1],[2,2]],[3,3]],[4,4]]",
     """
     [1,1]
     [2,2]
     [3,3]
     [4,4]
     """),
    ("[[[[3,0],[5,3]],[4,4]],[5,5]]",
     """
     [1,1]
     [2,2]
     [3,3]
     [4,4]
     [5,5]
     """),
    ("[[[[5,0],[7,4]],[5,5]],[6,6]]",
     """
     [1,1]
     [2,2]
     [3,3]
     [4,4]
     [5,5]
     [6,6]
     """),
    ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]",
     """
     [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
     [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
     [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
     [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
     [7,[5,[[3,8],[1,4]]]]
     [[2,[2,2]],[8,[8,1]]]
     [2,9]
     [1,[[[9,3],9],[[9,0],[0,7]]]]
     [[[5,[7,4]],7],1]
     [[[[4,2],2],6],[8,7]]
     """)
]

PART_1_ADDITION_EXAMPLE = """
  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
"""

PART_1_MAGNITUDE_EXAMPLES = [
    ("[9,1]", 29),
    ("[1,9]", 21),
    ("[[9,1],[1,9]]", 129),
    ("[[1,2],[[3,4],5]]", 143),
    ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
    ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
    ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
    ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
    ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
]

PART_1_HOMEWORK_ASSIGNMENT = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""


class Part1Tests(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual("[[1,2],[[3,4],5]]", day18.add("[1,2]", "[[3,4],5]"))

    def test_single_explode_action_examples(self):
        for before, after in PART_1_SINGLE_EXPLODE_ACTION_EXAMPLES:
            with self.subTest(before=before, after=after):
                self.assertEqual(after, day18.explode(before))

    def test_reduce(self):
        self.assertEqual(
            "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]",
            day18.reduce("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"))

    def test_reduce_steps(self):
        left, right = "[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"
        actual = None
        for line in utils.to_lines(PART_1_REDUCE_STEPS_EXAMPLE):
            action, expected = line.split(":")[0][6:], line[16:]
            if action == "addition":
                actual = day18.add(left, right, do_reduction=False)
            elif action == "explode":
                actual = day18.explode(actual)
            elif action == "split":
                actual = day18.split(actual)
            with self.subTest(action=action, expected=expected):
                self.assertEqual(expected, actual)

    def test_list_addition(self):
        for result, numbers in PART_1_LIST_EXAMPLES:
            numbers = utils.to_lines(numbers)
            numbers = [n.strip() for n in numbers]
            with self.subTest(result=result):
                self.assertEqual(result, day18.add_list(numbers))

    def test_list_addition_steps(self):
        for left, right, result in utils.group_lines(PART_1_ADDITION_EXAMPLE):
            left = left.lstrip()
            right = right[2:]
            result = result[2:]
            with self.subTest(result=result):
                self.assertEqual(result, day18.add(left, right))

    def test_magnitude(self):
        for (number, magnitude) in PART_1_MAGNITUDE_EXAMPLES:
            with self.subTest(number=number, magnitude=magnitude):
                self.assertEqual(magnitude, day18.magnitude(number))

    def test_homework_assignment(self):
        final_sum = day18.add_list(utils.to_lines(PART_1_HOMEWORK_ASSIGNMENT))
        self.assertEqual("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", final_sum)
        self.assertEqual(4140, day18.magnitude(final_sum))

    def test_with_input(self):
        self.assertEqual(4120, day18.magnitude(day18.add_list(utils.read_input_lines(18))))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3993, day18.part_2_answer(utils.to_lines(PART_1_HOMEWORK_ASSIGNMENT)))

    def test_with_input(self):
        self.assertEqual(4725, day18.part_2_answer(utils.read_input_lines(18)))
