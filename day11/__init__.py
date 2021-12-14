def part_1_answer(lines, steps):
    grid, width, height = parse_lines(lines)

    total_flashes = 0
    for _ in range(steps):
        grid, flashes = step(grid, width, height)
        total_flashes += flashes
    return total_flashes


def part_2_answer(lines):
    grid, width, height = parse_lines(lines)

    steps = 0
    while True:
        steps += 1
        grid, flashes = step(grid, width, height)
        if flashes == (width * height):
            return steps


def step(grid, width, height):
    new_grid = [line[:] for line in grid]

    for y in range(height):
        for x in range(width):
            new_grid[y][x] += 1

    to_flash = list()
    for y in range(height):
        for x in range(width):
            this = x, y
            if new_grid[y][x] > 9:
                to_flash.append(this)

    flashed = set(to_flash)

    while len(to_flash) > 0:
        x, y = to_flash.pop(0)
        for xn, yn in neighbours(x, y, width, height):
            neighbour = (xn, yn)
            if neighbour not in flashed:
                new_grid[yn][xn] += 1
                if new_grid[yn][xn] > 9:
                    to_flash.append(neighbour)
                    flashed.add(neighbour)
        new_grid[y][x] = 0

    return new_grid, len(flashed)


def neighbours(x, y, width, height):
    for yn in range(y - 1, y + 2):
        for xn in range(x - 1, x + 2):
            if (0 <= xn < width) and (0 <= yn < height) and not (x == xn and y == yn):
                yield xn, yn


def parse_lines(lines):
    grid = [[int(n) for n in line] for line in lines]
    width = len(lines[0])
    height = len(lines)
    return grid, width, height
