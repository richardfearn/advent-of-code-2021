from collections import defaultdict

import utils


def part_1_answer(lines):
    displays = parse_lines(lines)
    return sum(
        len(list(
            output_value for output_value in output_values
            if len(output_value) in (2, 4, 3, 7)))
        for _, output_values in displays)


def part_2_answer(lines):
    displays = parse_lines(lines)
    return sum(determine_output_values(display) for display in displays)


def determine_output_values(display):
    signal_patterns, output_values = display
    digit_segments = determine_digit_segments(signal_patterns)
    output_digits = [digit_segments.index(set(output_value)) for output_value in output_values]
    return int("".join(str(digit) for digit in output_digits))


def determine_digit_segments(signal_patterns):
    # pylint: disable=too-many-locals

    patterns_by_length = defaultdict(list)
    for pattern in signal_patterns:
        patterns_by_length[len(pattern)].append(set(pattern))

    one, four, seven, eight = [patterns_by_length[length][0] for length in (2, 4, 3, 7)]

    c_f = one
    (a,) = seven.difference(c_f)
    a_d_g = set.intersection(*patterns_by_length[5])
    (d,) = a_d_g.intersection(four)
    (g,) = a_d_g.difference({a, d})
    b_e = eight.difference(a_d_g).difference(c_f)
    (b,) = four.difference(a_d_g).difference(c_f)
    (e,) = b_e.difference(b)
    a_b_f_g = set.intersection(*patterns_by_length[6])
    (f,) = a_b_f_g.difference(a).difference(g).difference(b)
    (c,) = c_f.difference(f)

    return [
        {a, b, c, e, f, g},
        {c, f},
        {a, c, d, e, g},
        {a, c, d, f, g},
        {b, c, d, f},
        {a, b, d, f, g},
        {a, b, d, e, f, g},
        {a, c, f},
        {a, b, c, d, e, f, g},
        {a, b, c, d, f, g},
    ]


def parse_lines(lines):
    return [parse_line(line) for line in utils.to_lines(lines)]


def parse_line(line):
    signal_patterns, output_values = line.split(" | ")
    signal_patterns = signal_patterns.split(" ")
    output_values = output_values.split(" ")
    return signal_patterns, output_values
