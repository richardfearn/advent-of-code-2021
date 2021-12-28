from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
TargetArea = namedtuple("TargetArea", ["min", "max"])


def part_1_answer(target_area):
    highest_y_pos, _ = answer(target_area)
    return highest_y_pos


def part_2_answer(target_area):
    _, distinct_velocities = answer(target_area)
    return distinct_velocities


def answer(target_area):
    target_area = parse_target_area(target_area)

    highest_y_pos = 0
    distinct_velocities = 0

    for vx in range(1, target_area.max.x + 1):
        for vy in range(-140, 140):
            target_hit, highest_y_pos_for_velocity = fire(target_area, vx, vy)
            if target_hit:
                highest_y_pos = max(highest_y_pos, highest_y_pos_for_velocity)
                distinct_velocities += 1

    return highest_y_pos, distinct_velocities


def fire(target_area, vx, vy):
    max_height = 0
    x, y = (0, 0)

    while (y >= target_area.min.y) and (x <= target_area.max.x):

        x += vx
        y += vy

        max_height = max(max_height, y)

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if (target_area.min.x <= x <= target_area.max.x) and \
                (target_area.min.y <= y <= target_area.max.y):
            return True, max_height

    return False, max_height


def parse_target_area(target_area):
    target_area = target_area[13:]
    x, y = target_area.split(", ")
    (x_min, x_max), (y_min, y_max) = [[int(n) for n in axis[2:].split("..")] for axis in (x, y)]
    return TargetArea(Point(x_min, y_min), Point(x_max, y_max))
