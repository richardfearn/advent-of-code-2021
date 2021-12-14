from collections import defaultdict
from copy import copy

START, END = "start", "end"


def part_1_answer(lines):
    nodes, edges = parse_lines(lines)

    small_caves = [cave for cave in nodes if is_small_cave(cave)]

    initial = [START]
    to_visit = [initial]

    valid_paths = 0

    while len(to_visit) > 0:
        path_so_far = to_visit.pop(0)
        if path_so_far[-1] == END:
            valid_paths += 1
        else:
            for neighbour in edges[path_so_far[-1]]:
                if part_1_can_visit(neighbour, path_so_far, small_caves):
                    new_path = path_so_far + [neighbour]
                    to_visit.append(new_path)

    return valid_paths


def part_1_can_visit(neighbour, path_so_far, small_caves):
    if neighbour == START:
        return False
    if neighbour == END:
        return True
    if neighbour not in small_caves:
        return True
    return neighbour not in path_so_far


def part_2_answer(lines):
    nodes, edges = parse_lines(lines)

    small_caves = [cave for cave in nodes if is_small_cave(cave)]

    initial_path = [START]
    initial_small_cave_visits = {cave: 0 for cave in small_caves}

    return part_2_search(edges, initial_path, initial_small_cave_visits)


def part_2_search(edges, path_so_far, small_cave_visits):
    total_paths = 0
    if path_so_far[-1] == END:
        total_paths += 1
    else:
        for neighbour in edges[path_so_far[-1]]:
            if part_2_can_visit(neighbour, small_cave_visits):
                new_path, new_counts = part_2_next_node(path_so_far, small_cave_visits, neighbour)
                total_paths += part_2_search(edges, new_path, new_counts)
    return total_paths


def part_2_can_visit(neighbour, small_cave_visits):
    if neighbour == START:
        return False
    if neighbour == END:
        return True
    if neighbour not in small_cave_visits:
        return True
    if small_cave_visits[neighbour] == 0:
        return True
    return max(small_cave_visits.values()) < 2


def part_2_next_node(path_so_far, small_cave_visits, neighbour):
    new_path = path_so_far + [neighbour]

    new_visit_counts = copy(small_cave_visits)
    if neighbour in new_visit_counts:
        new_visit_counts[neighbour] += 1

    return new_path, new_visit_counts


def is_small_cave(cave):
    return (cave not in (START, END)) and (ord('a') <= ord(cave[0]) <= ord('z'))


def parse_lines(lines):
    nodes = set()
    edges = defaultdict(set)

    for line in lines:
        a, b = line.split("-")
        nodes.update({a, b})
        edges[a].add(b)
        edges[b].add(a)

    return nodes, edges
