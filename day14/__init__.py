from collections import defaultdict
from copy import copy


def part_1_answer(lines):
    return answer(lines, 10)


def part_2_answer(lines):
    return answer(lines, 40)


def answer(lines, steps):
    template, rules = parse_input(lines)
    letter_counts = do_pair_insertion_process(template, rules, steps)
    return max(letter_counts.values()) - min(letter_counts.values())


def do_pair_insertion_process(template, rules, steps):
    pair_counts = defaultdict(int)
    for i in range(0, len(template) - 1):
        pair = template[i:i + 2]
        pair_counts[pair] += 1

    for _ in range(steps):
        new_counts = copy(pair_counts)
        for pair, count in pair_counts.items():
            if (count > 0) and (pair in rules):
                new_pair_1 = pair[0] + rules[pair]
                new_pair_2 = rules[pair] + pair[1]
                new_counts[pair] -= count
                new_counts[new_pair_1] += count
                new_counts[new_pair_2] += count
        pair_counts = new_counts

    letter_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count
        letter_counts[pair[1]] += count
    letter_counts[template[0]] += 1
    letter_counts[template[-1]] += 1
    for letter in letter_counts.keys():
        letter_counts[letter] //= 2

    return letter_counts


def parse_input(lines):
    template = lines[0]
    rules = lines[2:]
    rules = [r.split(" -> ") for r in rules]
    rules = dict(rules)
    return template, rules
