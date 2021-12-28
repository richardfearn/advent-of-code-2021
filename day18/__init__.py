import math


class Pair:

    def __init__(self, left, right):
        self.parent = None
        self.children = [left, right]
        left.parent = right.parent = self

    def reset_links(self, parent=None, previous_number=None):
        self.parent = parent

        if previous_number is None:
            previous_number = [None]

        for child in self.children:
            child.reset_links(self, previous_number)

    def replace_child(self, old_child, new_child):
        for i in range(2):
            if self.children[i] == old_child:
                self.children[i] = new_child
                break

    def magnitude(self):
        return (3 * self.children[0].magnitude()) + (2 * self.children[1].magnitude())

    def __repr__(self):
        return "[%s,%s]" % (self.children[0], self.children[1])


class Number:

    def __init__(self, number):
        self.parent = None
        self.number = number
        self.left = self.right = None

    def reset_links(self, parent, previous_number):
        self.parent = parent

        if previous_number[0]:
            previous_number[0].right = self

        self.left = previous_number[0]
        self.right = None

        previous_number[0] = self

    def magnitude(self):
        return self.number

    def __repr__(self):
        return str(self.number)


def to_tree(number):
    if isinstance(number, str):
        return to_tree(eval(number))  # pylint: disable=eval-used
    if isinstance(number, list):
        return Pair(to_tree(number[0]), to_tree(number[1]))
    return Number(number)


def add(left, right, do_reduction=True):
    left_tree, right_tree = [to_tree(number) for number in (left, right)]
    total = _add(left_tree, right_tree, do_reduction)
    return repr(total)


def _add(left_tree, right_tree, do_reduction=True):
    total = Pair(left_tree, right_tree)
    if do_reduction:
        _reduce(total)
    return total


def reduce(number):
    tree = to_tree(number)
    _reduce(tree)
    return repr(tree)


def _reduce(tree):
    tree.reset_links()

    while True:

        if _explode(tree):
            continue

        if not _split(tree):
            break

    return tree


def explode(number):
    tree = to_tree(number)
    tree.reset_links()
    _explode(tree)
    return repr(tree)


def _explode(tree):
    pair_to_explode = find_pair_to_explode(tree)

    if pair_to_explode is not None:

        left, right = pair_to_explode.children

        replacement = Number(0)
        replacement.parent = pair_to_explode.parent

        if left.left:
            left.left.number += left.number
            left.left.right = replacement

        replacement.left = left.left
        replacement.right = right.right

        if right.right:
            right.right.number += right.number
            right.right.left = replacement

        pair_to_explode.parent.replace_child(pair_to_explode, replacement)

    return pair_to_explode is not None


def find_pair_to_explode(node, depth=0):
    if isinstance(node, Number):
        return None

    if isinstance(node, Pair) and depth == 4:
        return node

    for child in node.children:
        result = find_pair_to_explode(child, depth + 1)
        if result:
            return result

    return None


def split(number):
    tree = to_tree(number)
    tree.reset_links()
    _split(tree)
    return repr(tree)


def _split(tree):
    number_to_split = find_number_to_split(tree)

    if number_to_split is not None:

        num = number_to_split.number
        left, right = math.floor(num / 2), math.ceil(num / 2)

        new_left = Number(left)
        new_right = Number(right)
        new_pair = Pair(new_left, new_right)
        new_pair.parent = number_to_split.parent
        new_left.parent = new_right.parent = new_pair

        if number_to_split.left:
            number_to_split.left.right = new_left

        new_left.left = number_to_split.left
        new_left.right = new_right

        new_right.left = new_left
        new_right.right = number_to_split.right

        if number_to_split.right:
            number_to_split.right.left = new_right

        number_to_split.parent.replace_child(number_to_split, new_pair)

    return number_to_split is not None


def find_number_to_split(node):
    if isinstance(node, Number):
        if node.number >= 10:
            return node
        return None

    for child in node.children:
        result = find_number_to_split(child)
        if result:
            return result

    return None


def add_list(numbers):
    trees = [to_tree(number) for number in numbers]
    result = trees[0]
    for number in trees[1:]:
        result = _add(result, number)
    return repr(result)


def magnitude(number):
    return to_tree(number).magnitude()


def part_2_answer(numbers):
    largest_magnitude = 0
    for left in numbers:
        for right in numbers:
            if left != right:
                this_sum = _add(to_tree(left), to_tree(right))
                largest_magnitude = max(largest_magnitude, this_sum.magnitude())
    return largest_magnitude
