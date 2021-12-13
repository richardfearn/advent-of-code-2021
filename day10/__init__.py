LEFT = "([{<"
RIGHT = ")]}>"

CLOSING = dict(zip(LEFT, RIGHT))

CORRUPTED_POINTS = dict(zip(RIGHT, (3, 57, 1197, 25137)))

COMPLETION_POINTS = dict(zip(RIGHT, (1, 2, 3, 4)))


def part_1_answer(lines):
    return sum(syntax_error_score(line) for line in lines)


def syntax_error_score(line):
    stack = []
    for c in line:
        if c in LEFT:
            stack.append(c)
        else:
            expected = CLOSING[stack.pop()]
            if c != expected:
                return CORRUPTED_POINTS[c]
    return 0


def part_2_answer(lines):
    incomplete_lines = [line for line in lines if not is_corrupted(line)]
    scores = [completion_score(line) for line in incomplete_lines]
    scores = sorted(scores)
    return scores[len(scores) // 2]


def is_corrupted(line):
    return syntax_error_score(line) > 0


def completion_score(line):
    stack = []
    for c in line:
        if c in LEFT:
            stack.append(c)
        else:
            stack.pop()

    chars_to_add = [CLOSING[c] for c in reversed(stack)]

    score = 0
    for c in chars_to_add:
        score = score * 5 + COMPLETION_POINTS[c]

    return score
