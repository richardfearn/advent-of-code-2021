from collections import namedtuple

import utils

MatchingScanner = namedtuple("MatchingScanner", ["index", "beacons", "scanner_pos"])

AXIS_ORIENTATIONS = [
    (1, 3, -2),
    (-3, 1, -2),
    (-1, -3, -2),
    (3, -1, -2),
    (3, -2, 1),
    (2, 3, 1),
    (-3, 2, 1),
    (-2, -3, 1),
    (-2, 1, 3),
    (-1, -2, 3),
    (2, -1, 3),
    (1, 2, 3),
    (-3, -1, 2),
    (1, -3, 2),
    (3, 1, 2),
    (-1, 3, 2),
    (-1, 2, -3),
    (-2, -1, -3),
    (1, -2, -3),
    (2, 1, -3),
    (2, -3, -1),
    (3, 2, -1),
    (-2, 3, -1),
    (-3, -2, -1)
]


def part_1_answer(lines, num_overlap):
    scanners = parse_lines(lines)
    beacons, _ = merge_scanners(scanners, num_overlap)
    return len(beacons)


def part_2_answer(lines, num_overlap):
    scanners = parse_lines(lines)
    _, scanner_positions = merge_scanners(scanners, num_overlap)
    return find_max_distance(scanner_positions)


def merge_scanners(scanners, num_overlap):
    num_scanners = len(scanners)

    all_beacons = set()
    scanner_positions = set()
    unmatched = set(range(num_scanners))

    all_beacons.update(set(scanners[0]))
    scanner_positions.add((0, 0, 0))
    unmatched.remove(0)

    while len(unmatched) > 0:
        print("%d remaining" % len(unmatched))
        match = find_matching_scanner(all_beacons, scanners, unmatched, num_overlap)
        if match:
            all_beacons.update(match.beacons)
            scanner_positions.add(match.scanner_pos)
            unmatched.remove(match.index)

    return all_beacons, scanner_positions


def find_matching_scanner(all_beacons, scanners, unmatched, num_overlap):
    for index in unmatched:
        beacons = scanners[index]
        for rotated in orientations(beacons):
            for a in all_beacons:
                for b in rotated:
                    offset = tuple(b[i] - a[i] for i in range(3))
                    translated = set(tuple(c[i] - offset[i] for i in range(3)) for c in rotated)
                    overlap = all_beacons.intersection(translated)
                    if len(overlap) >= num_overlap:
                        return MatchingScanner(index=index, beacons=translated, scanner_pos=offset)
    return None


def orientations(beacons):
    for xyz in AXIS_ORIENTATIONS:
        axis_order = [abs(xyz[i]) - 1 for i in range(3)]
        axis_sign = [1 if xyz[i] > 0 else -1 for i in range(3)]
        yield [tuple(axis_sign[i] * b[axis_order[i]] for i in range(3)) for b in beacons]


def find_max_distance(scanner_positions):
    max_distance = 0
    for a in scanner_positions:
        for b in scanner_positions:
            if a != b:
                distance = sum(abs(b[i] - a[i]) for i in range(3))
                max_distance = max(max_distance, distance)
    return max_distance


def parse_lines(lines):
    scanners = utils.group_lines(lines)
    scanners = [beacons[1:] for beacons in scanners]
    scanners = [[parse_beacon(beacon) for beacon in beacons] for beacons in scanners]
    return scanners


def parse_beacon(line):
    xyz = [int(n) for n in line.split(",")]
    if len(xyz) == 2:
        xyz.append(0)
    return tuple(xyz)
