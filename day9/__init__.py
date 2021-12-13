def part_1_answer(lines):
    heights, width, height = parse_lines(lines)

    sum_of_risk_levels = 0
    for y in range(height):
        for x in range(width):
            neighbours = []
            for (xn, yn) in neighbours_of(x, y):
                if (0 <= yn < height) and (0 <= xn < width):
                    neighbours.append(heights[yn][xn])
            if heights[y][x] < min(neighbours):
                risk_level = 1 + heights[y][x]
                sum_of_risk_levels += risk_level

    return sum_of_risk_levels


def part_2_answer(lines):
    heights, width, height = parse_lines(lines)

    basin_sizes = []
    for y in range(height):
        for x in range(width):
            if 0 <= heights[y][x] < 9:
                basin_sizes.append(explore(heights, width, height, x, y))

    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def explore(heights, width, height, x, y):
    basin_size = 1
    heights[y][x] = -1
    for (xn, yn) in neighbours_of(x, y):
        if (0 <= yn < height) and (0 <= xn < width):
            if 0 <= heights[yn][xn] < 9:
                basin_size += explore(heights, width, height, xn, yn)
    return basin_size


def parse_lines(lines):
    heights = [[int(height) for height in list(line)] for line in lines]
    height = len(heights)
    width = len(heights[0])
    return heights, width, height


def neighbours_of(x, y):
    return (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)
