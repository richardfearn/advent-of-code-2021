from collections import defaultdict


def part_1_answer(lines):
    return count_points(lines, diagonals=False)


def part_2_answer(lines):
    return count_points(lines, diagonals=True)


def count_points(lines, diagonals):
    lines = [parse_line(line) for line in lines]

    grid = defaultdict(int)

    for ((x1, y1), (x2, y2)) in lines:

        if x1 == x2:  # vertical line
            if y1 > y2:
                (y1, y2) = (y2, y1)
            for y in range(y1, y2 + 1):
                grid[(x1, y)] += 1

        elif y1 == y2:  # horizontal line
            if x1 > x2:
                (x1, x2) = (x2, x1)
            for x in range(x1, x2 + 1):
                grid[(x, y1)] += 1

        elif diagonals:
            xd = 1 if (x2 > x1) else -1
            yd = 1 if (y2 > y1) else -1
            current = (x1, y1)
            end = (x2, y2)
            while True:
                grid[current] += 1
                if current == end:
                    break
                current = (current[0] + xd, current[1] + yd)

    return len([num_lines for num_lines in grid.values() if num_lines > 1])


def parse_line(line):
    line = line.split(" -> ")
    line = [[int(n) for n in line.split(",")] for line in line]
    return line
