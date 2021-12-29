from collections import namedtuple

import utils

Point = namedtuple("Point", ["x", "y"])


def part_1_answer(lines, steps):
    algorithm, image = parse_input(lines)

    image_map = to_map(image)
    default_pixel_value = 0

    for _ in range(steps):
        image_map = enhance(image_map, algorithm, default_pixel_value)
        default_pixel_value = algorithm[default_pixel_value * 511]

    return list(image_map.values()).count(1)


def to_map(image):
    width, height = len(image[0]), len(image)
    image_map = {}
    for y in range(0, height):
        for x in range(0, width):
            image_map[Point(x, y)] = 1 if image[y][x] == "#" else 0
    return image_map


def enhance(image_map, algorithm, default_pixel_value):
    (x_min, x_max), (y_min, y_max) = find_extent(image_map)

    new_map = {}
    for y in range(y_min - 1, y_max + 2):
        for x in range(x_min - 1, x_max + 2):
            pixels = get_pixels_around(x, y, image_map, default_pixel_value)
            algorithm_index = int("".join(str(n) for n in pixels), 2)
            new_map[Point(x, y)] = algorithm[algorithm_index]

    return new_map


def find_extent(image_map):
    pixels = image_map.keys()
    x_vals = set(p.x for p in pixels)
    y_vals = set(p.y for p in pixels)
    return ((min(vals), max(vals)) for vals in (x_vals, y_vals))


def get_pixels_around(x, y, image_map, default_pixel_value):
    pixels = []
    for sy in range(y - 1, y + 2):
        for sx in range(x - 1, x + 2):
            pixels.append(image_map.get(Point(sx, sy), default_pixel_value))
    return pixels


def parse_input(lines):
    groups = utils.group_lines(lines)
    algorithm, image = groups[0], groups[1]
    algorithm = "".join(algorithm)
    algorithm = [1 if c == "#" else 0 for c in algorithm]
    return algorithm, image
