def step(lines):
    height = len(lines)
    width = len(lines[0])

    new_grid = [list(line) for line in lines]

    for y in range(height):
        for x in range(width):
            if lines[y][x] == ">":
                xn = (x + 1) % width
                yn = y
                if lines[yn][xn] == ".":
                    new_grid[y][x] = "."
                    new_grid[yn][xn] = ">"

    lines = new_grid

    new_grid = [line[:] for line in lines]

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "v":
                xn = x
                yn = (y + 1) % height
                if lines[yn][xn] == ".":
                    new_grid[y][x] = "."
                    new_grid[yn][xn] = "v"

    new_grid = ["".join(line) for line in new_grid]
    return new_grid


def part_1_answer(lines):
    before = lines
    num_steps = 0
    changing = True

    while changing:
        num_steps += 1
        after = step(before)
        changing = (before != after)
        before = after

    return num_steps
